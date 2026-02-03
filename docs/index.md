# ytnb-embed

<div align="center" markdown>

[![PyPI version](https://img.shields.io/pypi/v/ytnb-embed.svg)](https://pypi.org/project/ytnb-embed/)
[![Python Version](https://img.shields.io/pypi/pyversions/ytnb-embed.svg)](https://pypi.org/project/ytnb-embed/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://pepy.tech/badge/ytnb-embed)](https://pepy.tech/project/ytnb-embed)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![CI](https://github.com/aatansen/ytnb-embed/actions/workflows/ci.yml/badge.svg)](https://github.com/aatansen/ytnb-embed/actions/workflows/ci.yml)

**A lightweight, privacy-focused Python package for embedding YouTube videos in Jupyter Notebooks**

</div>

---

## Overview

`ytnb-embed` provides a simple and elegant way to embed YouTube videos directly in Jupyter Notebooks. Built with privacy and simplicity in mind, it uses YouTube's privacy-enhanced mode (`youtube-nocookie.com`) to protect user privacy while maintaining full video functionality.

Perfect for data scientists, educators, and researchers who want to enrich their notebooks with video content without compromising on privacy or simplicity.

## Features

- 🎥 **One-line embedding** - Embed any YouTube video with a single function call
- 🔒 **Privacy-first** - Uses `youtube-nocookie.com` for enhanced privacy protection
- 📐 **Fully customizable** - Adjust video player dimensions to fit your needs
- 🛡️ **Smart URL parsing** - Handles all YouTube URL formats automatically
- 📝 **Built-in logging** - Comprehensive logging for debugging and monitoring
- ✅ **Type hints** - Full type annotation support for better IDE integration
- 🧪 **Well tested** - Includes unit and integration tests
- 🚀 **Lightweight** - Minimal dependencies, maximum performance

## Quick Installation

  ```sh
  pip install ytnb-embed
  ```

## Quick Example

  ```py
  from ytnb_embed import embed_yt

  # Embed a YouTube video
  embed_yt("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
  ```

## Next Steps

- [Installation Guide](installation.md) - Detailed installation instructions
- [Quick Start](quick-start.md) - Get started in minutes
- [Usage Guide](usage/basic.md) - Learn all the features
- [API Reference](api.md) - Complete API documentation