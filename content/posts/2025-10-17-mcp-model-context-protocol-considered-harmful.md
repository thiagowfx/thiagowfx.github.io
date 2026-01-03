---
title: "MCP: model context protocol considered harmful"
date: 2025-10-17T13:07:03+02:00
tags:
  - ai
  - dev
---

[Previously]({{< ref "2025-10-08-claude-code-adding-my-first-mcp-server" >}}).

I configured my [Claude Code](https://www.claude.com/product/claude-code)
instance at work to include exactly 3 MCP servers:

- github
- playwright (browser automation / testing)
- atlassian (JIRA, Confluence, etc)

Sensible, right? It's not like I'm a heavy user of MCPs. I mostly care about:

- PR introspection / creation
- occasional unit / integration testing in the browser
- JIRA (read access)

I didn't even have the opportunity to add an MCP for Docker or Kubernetes yet.

And yet:

```
% claude
> /context
  ⎿
      Context Usage
     ⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛁   claude-sonnet-4-5-20250929 · 133k/200k tokens (67%)
     ⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛁
     ⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛁   ⛁ System prompt: 2.5k tokens (1.2%)
     ⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛁   ⛁ System tools: 13.8k tokens (6.9%)
     ⛁ ⛁ ⛁ ⛁ ⛀ ⛀ ⛶ ⛶ ⛶ ⛶   ⛁ MCP tools: 71.7k tokens (35.9%)
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   ⛁ Custom agents: 209 tokens (0.1%)
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   ⛁ Messages: 8 tokens (0.0%)
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛝ ⛝ ⛝   ⛶ Free space: 67k (33.4%)
     ⛝ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝   ⛝ Autocompact buffer: 45.0k tokens (22.5%)
     ⛝ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝

     MCP tools · /mcp
     └ mcp__playwright__browser_close (playwright): 573 tokens
     └ mcp__playwright__browser_resize (playwright): 622 tokens
     └ mcp__playwright__browser_console_messages (playwright): 595 tokens
     └ mcp__playwright__browser_handle_dialog (playwright): 626 tokens
     └ mcp__playwright__browser_evaluate (playwright): 671 tokens
     └ mcp__playwright__browser_file_upload (playwright): 626 tokens
     └ mcp__playwright__browser_fill_form (playwright): 776 tokens
     └ mcp__playwright__browser_install (playwright): 591 tokens
     └ mcp__playwright__browser_press_key (playwright): 620 tokens
     └ mcp__playwright__browser_type (playwright): 728 tokens
     └ mcp__playwright__browser_navigate (playwright): 598 tokens
     └ mcp__playwright__browser_navigate_back (playwright): 578 tokens
     └ mcp__playwright__browser_network_requests (playwright): 580 tokens
     └ mcp__playwright__browser_take_screenshot (playwright): 826 tokens
     └ mcp__playwright__browser_snapshot (playwright): 584 tokens
     └ mcp__playwright__browser_click (playwright): 753 tokens
     └ mcp__playwright__browser_drag (playwright): 709 tokens
     └ mcp__playwright__browser_hover (playwright): 636 tokens
     └ mcp__playwright__browser_select_option (playwright): 684 tokens
     └ mcp__playwright__browser_tabs (playwright): 652 tokens
     └ mcp__playwright__browser_wait_for (playwright): 650 tokens
     └ mcp__atlassian__atlassianUserInfo (atlassian): 583 tokens
     └ mcp__atlassian__getAccessibleAtlassianResources (atlassian): 592 tokens
     └ mcp__atlassian__getConfluenceSpaces (atlassian): 1.1k tokens
     └ mcp__atlassian__getConfluencePage (atlassian): 830 tokens
     └ mcp__atlassian__getPagesInConfluenceSpace (atlassian): 975 tokens
     └ mcp__atlassian__getConfluencePageFooterComments (atlassian): 873 tokens
     └ mcp__atlassian__getConfluencePageInlineComments (atlassian): 905 tokens
     └ mcp__atlassian__getConfluencePageDescendants (atlassian): 799 tokens
     └ mcp__atlassian__createConfluencePage (atlassian): 895 tokens
     └ mcp__atlassian__updateConfluencePage (atlassian): 911 tokens
     └ mcp__atlassian__createConfluenceFooterComment (atlassian): 834 tokens
     └ mcp__atlassian__createConfluenceInlineComment (atlassian): 1.0k tokens
     └ mcp__atlassian__searchConfluenceUsingCql (atlassian): 911 tokens
     └ mcp__atlassian__getJiraIssue (atlassian): 869 tokens
     └ mcp__atlassian__editJiraIssue (atlassian): 803 tokens
     └ mcp__atlassian__createJiraIssue (atlassian): 1.2k tokens
     └ mcp__atlassian__getTransitionsForJiraIssue (atlassian): 857 tokens
     └ mcp__atlassian__transitionJiraIssue (atlassian): 1.3k tokens
     └ mcp__atlassian__lookupJiraAccountId (atlassian): 708 tokens
     └ mcp__atlassian__searchJiraIssuesUsingJql (atlassian): 856 tokens
     └ mcp__atlassian__addCommentToJiraIssue (atlassian): 913 tokens
     └ mcp__atlassian__getJiraIssueRemoteIssueLinks (atlassian): 919 tokens
     └ mcp__atlassian__getVisibleJiraProjects (atlassian): 943 tokens
     └ mcp__atlassian__getJiraProjectIssueTypesMetadata (atlassian): 794 tokens
     └ mcp__atlassian__getJiraIssueTypeMetaWithFields (atlassian): 777 tokens
     └ mcp__atlassian__search (atlassian): 640 tokens
     └ mcp__atlassian__fetch (atlassian): 685 tokens
     └ mcp__github__add_comment_to_pending_review (github): 914 tokens
     └ mcp__github__add_issue_comment (github): 644 tokens
     └ mcp__github__add_sub_issue (github): 701 tokens
     └ mcp__github__assign_copilot_to_issue (github): 724 tokens
     └ mcp__github__create_and_submit_pull_request_review (github): 708 tokens
     └ mcp__github__create_branch (github): 638 tokens
     └ mcp__github__create_issue (github): 732 tokens
     └ mcp__github__create_or_update_file (github): 768 tokens
     └ mcp__github__create_pending_pull_request_review (github): 698 tokens
     └ mcp__github__create_pull_request (github): 719 tokens
     └ mcp__github__create_repository (github): 661 tokens
     └ mcp__github__delete_file (github): 664 tokens
     └ mcp__github__delete_pending_pull_request_review (github): 650 tokens
     └ mcp__github__fork_repository (github): 613 tokens
     └ mcp__github__get_commit (github): 728 tokens
     └ mcp__github__get_file_contents (github): 717 tokens
     └ mcp__github__get_issue (github): 627 tokens
     └ mcp__github__get_issue_comments (github): 690 tokens
     └ mcp__github__get_label (github): 616 tokens
     └ mcp__github__get_latest_release (github): 594 tokens
     └ mcp__github__get_me (github): 576 tokens
     └ mcp__github__get_release_by_tag (github): 634 tokens
     └ mcp__github__get_tag (github): 615 tokens
     └ mcp__github__get_team_members (github): 616 tokens
     └ mcp__github__get_teams (github): 589 tokens
     └ mcp__github__list_branches (github): 660 tokens
     └ mcp__github__list_commits (github): 773 tokens
     └ mcp__github__list_issue_types (github): 580 tokens
     └ mcp__github__list_issues (github): 886 tokens
     └ mcp__github__list_label (github): 637 tokens
     └ mcp__github__list_pull_requests (github): 821 tokens
     └ mcp__github__list_releases (github): 660 tokens
     └ mcp__github__list_sub_issues (github): 677 tokens
     └ mcp__github__list_tags (github): 661 tokens
     └ mcp__github__merge_pull_request (github): 695 tokens
     └ mcp__github__pull_request_read (github): 879 tokens
     └ mcp__github__push_files (github): 739 tokens
     └ mcp__github__remove_sub_issue (github): 671 tokens
     └ mcp__github__reprioritize_sub_issue (github): 768 tokens
     └ mcp__github__request_copilot_review (github): 640 tokens
     └ mcp__github__search_code (github): 777 tokens
     └ mcp__github__search_issues (github): 824 tokens
     └ mcp__github__search_pull_requests (github): 830 tokens
     └ mcp__github__search_repositories (github): 817 tokens
     └ mcp__github__search_users (github): 760 tokens
     └ mcp__github__submit_pending_pull_request_review (github): 719 tokens
     └ mcp__github__update_issue (github): 852 tokens
     └ mcp__github__update_pull_request (github): 786 tokens
     └ mcp__github__update_pull_request_branch (github): 655 tokens
```

The Sonnet 4 model has a context window of 200k tokens.

These 3 MCP servers, alone, consume about one third of them. **36%**!

If you account for system tools + the system prompt in the mix, practically half
of the total available context window is already gone.

MCP tool definitions are wasteful, taking valuable ~~real~~ virtual estate,
distracting the model, increasing overall costs.

![south park agent context window aaaand it's gone](https://i.imgflip.com/a9djwa.jpg)

As [Simon Willison](https://simonwillison.net/2025/Oct/14/agentic-engineering/)
already noted from [Peter Steinberger](https://steipete.me/posts/just-talk-to-it):

> He shares my preference for CLI utilities over MCPs:
>
> > I can just refer to a cli by name. I don't need any explanation in my agents
> > file. The agent will try $randomcrap on the first call, the cli will present
> > the help menu, context now has full info how this works and from now on we
> > good. I don't have to pay a price for any tools, unlike MCPs which are a
> > constant cost and garbage in my context. Use GitHub's MCP and see 23k tokens
> > gone. Heck, they did make it better because it was almost 50.000 tokens when
> > it first launched. Or use the gh cli which has basically the same feature
> > set, models already know how to use it, and pay zero context tax.

To me this feels comparable to using a full-blown desktop environment in Linux
Desktop versus rolling your tiling window manager and building from scratch
an environment tailored to your own needs.

Stay safe from the bloat out there.

**Update(2025-10-18)**: See also [Skills c:ompared to
MCP](https://simonwillison.net/2025/Oct/16/claude-skills/#skills-compared-to-mcp).
