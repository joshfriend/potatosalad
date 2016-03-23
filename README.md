# John Cena Placeholder Image Generator

[![Build Status][travis-badge]][travis-status]
[![Coverage Status][coveralls-badge]][coveralls-status]

## Instructions
Potatosalad works like most other placeholder image generator sites, like
[Place Harold][placeharold] or [Placekitten][placekitten]. Put the image width
and height (and optionally, a format) in the URL:

`https://potatosalad.herokuapp.com/<width>/<height>.<format>`

For example:

`https://potatosalad.herokuapp.com/320/240.jpg`

Would give you a picture like this:

![example](https://potatosalad.herokuapp.com/320/240.jpg)

### Supported Image Formats

The default format (if none is given) is `.jpg`, but the following are
supported:

* `jpg` and `jpeg`
* `png`
* `bmp`

[travis-badge]: http://img.shields.io/travis/joshfriend/potatosalad/master.svg
[travis-status]: https://travis-ci.org/joshfriend/potatosalad
[coveralls-status]: https://coveralls.io/r/joshfriend/potatosalad
[coveralls-badge]: http://img.shields.io/coveralls/joshfriend/potatosalad/master.svg
[placeharold]: http://placeharold.com/
[placekitten]: https://placekitten.com/
