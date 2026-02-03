## Quick Start

  ```py
  from ytnb_embed import embed_yt

  # Embed a YouTube video with default dimensions (780x440)
  embed_yt("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

  # Customize the video player size
  embed_yt("https://www.youtube.com/watch?v=dQw4w9WgXcQ", width=640, height=360)
  ```

That's it! The video will be embedded directly in your Jupyter Notebook cell output.