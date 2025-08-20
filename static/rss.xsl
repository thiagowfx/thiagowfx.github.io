<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:atom="http://www.w3.org/2005/Atom">
  <xsl:output method="html" doctype-public="-//W3C//DTD HTML 4.01 Transitional//EN" doctype-system="http://www.w3.org/TR/html4/loose.dtd" indent="yes"/>

  <xsl:template match="/">
    <html>
      <head>
        <title><xsl:value-of select="rss/channel/title"/> - RSS Feed</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1"/>
        <style type="text/css">
          :root {
            --color-gray: #888;
            --color-grayer: #666;
            --font-title: "Inter", "Fira Sans", "Lato", system-ui, -apple-system, BlinkMacSystemFont, "Avenir Next", "Avenir", "Segoe UI", "Helvetica Neue", Helvetica, Ubuntu, Roboto, Noto, Cantarell, Arial, sans-serif;
            --font-body: "Crimson Pro", "Vollkorn", "Alegreya", "Iowan Old Style", "Apple Garamond", "Baskerville", "Times New Roman", "Noto Serif", "Droid Serif", "Times", "Source Serif Pro", serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
            --font-code: "Fira Code", "PT Mono", "IBM Plex Mono", Menlo, Consolas, Monaco, "Liberation Mono", "Ubuntu Mono", "Lucida Console", monospace;
          }

          body {
            font-family: var(--font-body);
            font-size: 21px;
            line-height: 1.5;
            color: #444;
            max-width: 840px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fffcf0;
            word-wrap: break-word;
            overflow-wrap: break-word;
            -webkit-text-size-adjust: 100%;
          }

          .header {
            border-bottom: 2px solid #ddd;
            margin-bottom: 30px;
            padding-bottom: 20px;
          }

          .header h1 {
            font-family: var(--font-title);
            margin: 0;
            color: #222;
            font-size: 2.5rem;
            line-height: 1.2;
          }

          .header p {
            margin: 10px 0 0;
            color: var(--color-gray);
            font-size: 1.1em;
          }

          .feed-info {
            background: #f2f2f2;
            border: 1px solid #e0e0e0;
            border-radius: 5px;
            padding: 20px;
            margin-bottom: 30px;
          }

          .feed-info h2 {
            font-family: var(--font-title);
            margin-top: 0;
            color: #222;
            line-height: 1.2;
          }

          .feed-url {
            background: #fffcf0;
            border: 1px solid #ddd;
            padding: 10px;
            border-radius: 3px;
            font-family: var(--font-code);
            word-break: break-all;
          }

          .item {
            border-bottom: 1px solid #eee;
            padding: 20px 0;
          }

          .item:last-child {
            border-bottom: none;
          }

          .item h3 {
            font-family: var(--font-title);
            margin: 0 0 10px;
            font-size: 1.75rem;
            line-height: 1.2;
          }

          .item h3 a {
            color: #3273dc;
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
            color: #444;
            line-height: 1.5;
          }

          .item-description p:first-child {
            margin-top: 0;
          }

          .item-description p:last-child {
            margin-bottom: 0;
          }

          .footer {
            font-family: var(--font-title);
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #ddd;
            text-align: center;
            color: var(--color-gray);
            font-size: smaller;
          }

          .footer a {
            color: #3273dc;
          }

          @media (prefers-color-scheme: dark) {
            body {
              background-color: #01242e;
              color: #ddd;
            }

            .header h1,
            .feed-info h2,
            .item h3 {
              color: #eee;
            }

            .header {
              border-bottom-color: #444;
            }

            .feed-info {
              background: #333;
              border-color: #444;
            }

            .feed-url {
              background: #01242e;
              border-color: #444;
            }

            .item {
              border-bottom-color: #444;
            }

            .item h3 a {
              color: #8cc2dd;
            }

            .item-description {
              color: #ddd;
            }

            .footer {
              border-top-color: #444;
            }

            .footer a {
              color: #8cc2dd;
            }
          }

          @media (max-width: 600px) {
            body {
              padding: 15px;
            }

            .header h1 {
              font-size: 2rem;
            }

            .item h3 {
              font-size: 1.5rem;
            }
          }
        </style>
      </head>
      <body>
        <div class="header">
          <h1><xsl:value-of select="rss/channel/title"/></h1>
          <p><xsl:value-of select="rss/channel/description"/></p>
        </div>

        <div class="feed-info">
          <h2>📡 RSS Feed</h2>
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
                <strong>By:</strong> <xsl:value-of select="author"/> •
              </xsl:if>
              <strong>Published:</strong> <xsl:value-of select="pubDate"/>
            </div>

            <div class="item-description">
              <xsl:value-of select="description" disable-output-escaping="yes"/>
            </div>
          </div>
        </xsl:for-each>

        <div class="footer">
          <p>
            Generated by <a href="https://gohugo.io/" target="_blank">Hugo</a> •
            Last updated: <xsl:value-of select="rss/channel/lastBuildDate"/>
          </p>
          <xsl:if test="rss/channel/copyright">
            <p><xsl:value-of select="rss/channel/copyright"/></p>
          </xsl:if>
        </div>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>