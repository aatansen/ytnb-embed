## Advanced Usages

### Custom Player Dimensions

Tailor the video player size to your notebook layout:

  ```py
  # Large player for presentations
  embed_yt("https://www.youtube.com/watch?v=VIDEO_ID", width=1024, height=576)

  # Standard 16:9 aspect ratio
  embed_yt("https://www.youtube.com/watch?v=VIDEO_ID", width=854, height=480)

  # Compact player for documentation
  embed_yt("https://www.youtube.com/watch?v=VIDEO_ID", width=560, height=315)
  ```
