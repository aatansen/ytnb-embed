## Privacy & Security

### Privacy-Enhanced Mode

`ytnb-embed` uses YouTube's privacy-enhanced mode by default. Videos are embedded from `youtube-nocookie.com`, which provides:

- **Reduced tracking** - YouTube doesn't store information about visitors unless they play the video
- **No third-party cookies** - Cookies are only set when the user interacts with the video
- **Same functionality** - All standard YouTube features remain available

### Security Features

- **URL validation** - Regex-based validation prevents injection attacks
- **Sandboxed iframe** - Videos load in isolated iframe contexts
- **Strict referrer policy** - `strict-origin-when-cross-origin` prevents data leakage
