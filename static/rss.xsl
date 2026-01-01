<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:atom="http://www.w3.org/2005/Atom">
  <xsl:output method="html" doctype-public="-//W3C//DTD HTML 4.01 Transitional//EN" doctype-system="http://www.w3.org/TR/html4/loose.dtd" indent="yes"/>

  <xsl:template match="/">
    <html>
      <head>
        <title><xsl:value-of select="rss/channel/title"/> - RSS Feed</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1"/>
        <link rel="stylesheet" href="/theme.css"/>
        <style type="text/css">
          .header {
            border-bottom: 2px solid var(--border-color);
            margin-bottom: 30px;
            padding-bottom: 20px;
          }

          .header h1 {
            margin: 0;
            display: flex;
            align-items: center;
            column-gap: 10px;
          }

          .header h1 a {
            color: inherit;
            text-decoration: none;
            display: flex;
            align-items: center;
            column-gap: 10px;
          }

          .header h1 a:hover {
            text-decoration: underline;
          }

          .header img {
            width: 32px;
            height: 32px;
          }

          .header p {
            margin: 10px 0 0;
            color: var(--color-gray);
            font-size: 1.1em;
          }

          .feed-info {
            background: var(--code-bg);
            border: 1px solid var(--border-color);
            border-radius: 5px;
            padding: 20px;
            margin-bottom: 30px;
          }

          .feed-info h2 {
            margin-top: 0;
          }

          .feed-url {
            background: var(--bg-color);
            border: 1px solid var(--border-color);
            padding: 10px;
            border-radius: 3px;
            word-break: break-all;
          }

          .item {
            border-bottom: 1px solid var(--border-color);
            padding: 20px 0;
            opacity: 0.8;
          }

          .item:last-child {
            border-bottom: none;
          }

          .item h3 {
            margin: 0 0 10px;
          }

          .item h3 a {
            text-decoration: none;
          }

          .item h3 a:hover {
            text-decoration: underline;
          }

          .item-meta {
            color: var(--color-gray);
            font-size: 0.9em;
            margin-bottom: 15px;
            font-style: italic;
          }

          .item-description {
            color: var(--text-color);
            line-height: 1.5;
          }

          .item-description p:first-child {
            margin-top: 0;
          }

          .item-description p:last-child {
            margin-bottom: 0;
          }

          .item-description pre {
            background: var(--code-bg);
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            border: 1px solid var(--border-color);
          }

          .item-description pre code {
            background: none;
            padding: 0;
          }

          .footer {
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid var(--border-color);
            text-align: center;
            color: var(--color-gray);
            font-size: smaller;
          }

          .footer p {
            margin: 8px 0;
          }

          .footer a[href^="http"]:after {
            content: " ↗";
            font-size: 0.8em;
          }
        </style>
      </head>
      <body>
        <div class="header">
          <h1>
            <a href="{rss/channel/link}">
              <img src="/thiagowfx.webp" alt="thiagowfx's avatar"/>
              <xsl:value-of select="rss/channel/title"/>
            </a>
          </h1>
          <p><xsl:value-of select="rss/channel/description"/></p>
        </div>

        <div class="feed-info">
          <h2 style="display: flex; align-items: center; gap: 0.25em;">
            RSS feed
            <svg xmlns="http://www.w3.org/2000/svg" aria-label="RSS" role="img" viewBox="0 0 512 512" height="1em" width="1em">
              <path d="m0 0H512V512H0" fill="#f80"/>
              <path fill="#fff" d="m109 271A132 133 0 01241 403h60A192 193 0 00109 211v-54A246 247 0 01355 403h60A306 307 0 00109 97m35 235a35 35 0 102 0"/>
            </svg>
          </h2>
          <p>This is an RSS feed. You can subscribe to it using your favorite RSS reader to get updates when new posts are published.</p>
          <p><strong>Feed URL:</strong></p>
          <div class="feed-url">
            <xsl:value-of select="rss/channel/atom:link/@href"/>
          </div>
          <p style="margin-bottom: 0;">
            <a href="{rss/channel/link}">← Back to website</a>
          </p>
        </div>

        <xsl:for-each select="rss/channel/item">
          <div class="item">
            <h3>
              <a href="{link}" target="_blank">
                <xsl:value-of select="title"/>
              </a>
            </h3>

            <div class="item-meta">
              <xsl:if test="author">
                <strong>By: </strong> <a href="mailto:{substring-before(author, ' (')}"><xsl:value-of select="substring-before(substring-after(author, ' ('), ')')"/></a> •
              </xsl:if>
              <strong>Published: </strong> <xsl:value-of select="pubDate"/>
            </div>

            <div class="item-description">
              <xsl:value-of select="description" disable-output-escaping="yes"/>
            </div>
          </div>
        </xsl:for-each>

        <div class="footer">
          <p>
            Generated by <a href="https://gohugo.io/">Hugo</a> •
            Last updated: <xsl:value-of select="rss/channel/lastBuildDate"/>
          </p>
          <xsl:if test="rss/channel/copyright">
            <p>
              © 2021 - 2025 Thiago Perrotta ·
              <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">some rights reserved</a> ·
              a fork of <a href="https://github.com/janraasch/hugo-bearblog/">hugo ʕ•ᴥ•ʔ bear</a>
            </p>
          </xsl:if>
        </div>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
