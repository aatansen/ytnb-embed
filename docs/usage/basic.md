## Basic Usages

### Supported URL Formats

`ytnb-embed` intelligently parses all standard YouTube URL formats:

```py
from ytnb_embed import embed_yt

# Standard watch URL
embed_yt("https://www.youtube.com/watch?v=VIDEO_ID")

# Short URL
embed_yt("https://youtu.be/VIDEO_ID")

# Embed URL
embed_yt("https://www.youtube.com/embed/VIDEO_ID")

# Direct video URL
embed_yt("https://www.youtube.com/v/VIDEO_ID")

# URLs with timestamps and other parameters
embed_yt("https://www.youtube.com/watch?v=VIDEO_ID&t=30s")
```
