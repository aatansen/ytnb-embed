## API Reference

### `embed_yt(url, width=780, height=440)`

Embeds a YouTube video in a Jupyter Notebook using an iframe.

#### Parameters

| Parameter | Type  | Default    | Description                              |
| --------- | ----- | ---------- | ---------------------------------------- |
| `url`     | `str` | *required* | YouTube video URL in any standard format |
| `width`   | `int` | `780`      | Width of the video player in pixels      |
| `height`  | `int` | `440`      | Height of the video player in pixels     |

#### Returns

- `str`: Returns `"success"` when the video is successfully embedded

#### Raises

- `InvalidURLException`: Raised when the provided URL is not a valid YouTube URL
- `Exception`: Raised for other unexpected errors during embedding

#### Example

```py
result = embed_yt("https://www.youtube.com/watch?v=VIDEO_ID", width=800, height=450)
# result == "success"
```
