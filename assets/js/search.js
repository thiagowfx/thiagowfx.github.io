const fetchWithTimeout = (url, timeout = 5000) =>
  fetch(url, { signal: AbortSignal.timeout(timeout) });

const fetchIndex = (url, retries = 1) =>
  fetchWithTimeout(url).catch((err) =>
    retries > 0 ? fetchWithTimeout(url) : Promise.reject(err),
  );

const termToRegex = (term) => {
  const escaped = term.replace(/[.+?^${}()|[\]\\]/g, "\\$&");
  return new RegExp(escaped.replace(/\*/g, "[^\\s]*"), "i");
};

const matchesTerm = (text, term) =>
  term.includes("*") ? termToRegex(term).test(text) : text.includes(term);

export class SearchIndex {
  constructor(langPath) {
    this.langPath = langPath;
    this.posts = null;
    this.content = null;
    this.postsPromise = null;
    this.contentPromise = null;
  }

  loadPosts() {
    if (this.posts !== null) return Promise.resolve(this.posts);
    if (this.postsPromise !== null) return this.postsPromise;

    this.postsPromise = fetchIndex(`${this.langPath}/search/index.json`)
      .then((response) => response.json())
      .then((posts) => {
        this.posts = posts;
        return posts;
      })
      .finally(() => {
        this.postsPromise = null;
      });
    return this.postsPromise;
  }

  loadContent() {
    if (this.content !== null) return Promise.resolve(this.content);
    if (this.contentPromise !== null) return this.contentPromise;

    this.contentPromise = fetchIndex(
      `${this.langPath}/search-content/index.json`,
    )
      .then((response) => response.json())
      .then((posts) => {
        this.content = new Map(
          posts.map((post) => [post.url, (post.content ?? "").toLowerCase()]),
        );
        return this.content;
      })
      .finally(() => {
        this.contentPromise = null;
      });
    return this.contentPromise;
  }

  search(query, posts = this.posts, includeContent = false) {
    const terms = query.toLowerCase().trim().split(/\s+/).filter(Boolean);
    const results = [];

    for (const post of posts ?? []) {
      const title = (post.title ?? "").toLowerCase();
      const summary = (post.summary ?? "").toLowerCase();
      const tags = (post.tags ?? []).map((tag) => tag.toLowerCase()).join(" ");
      const content = includeContent ? (this.content?.get(post.url) ?? "") : "";
      let score = 0;

      for (const term of terms) {
        const inTitle = matchesTerm(title, term);
        const inSummary = matchesTerm(summary, term);
        const inTags = matchesTerm(tags, term);
        const inContent = includeContent && matchesTerm(content, term);

        if (!inTitle && !inSummary && !inTags && !inContent) {
          score = null;
          break;
        }

        if (inTitle) score += 10;
        if (inTags) score += 5;
        if (inSummary || inContent) score += 1;
      }

      if (score !== null) results.push({ post, score });
    }

    return results.sort(
      (a, b) => b.score - a.score || b.post.date.localeCompare(a.post.date),
    );
  }
}
