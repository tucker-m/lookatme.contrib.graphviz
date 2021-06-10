# lookatme.contrib.graphviz

Renders ASCII art of Graphviz Dot graphs

## Installation

This plugin requires graph-easy, a perl module, to be installed in your system
and runnable by calling `graph-easy` from your terminal.

### Installing graph-easy

#### Ubuntu

On Ubuntu, you can do:

```
apt install libgraph-easy-perl
```

`graph-easy` should then be available to you.

#### Mac

On Mac, you can do:

```
brew install cpanminus
cpan Graph::Easy
```

The binary will be in `/opt/local/libexec/perl5.12/sitebin/graph-easy`
or `/usr/local/Cellar/perl/5.32.1_1/bin/graph-easy`. (You might need
to adjust the perl version number in those paths.) If the `graph-easy`
command doesn't do anything, use a symlink to add it to somewhere on your
PATH. E.g.:

```bash
ln -s /usr/local/Cellar/perl/5.32.1_1/bin/graph-easy /bin/graph-easy
```

### Installing this lookatme plugin

```bash
pip install ./path/to/lookatme.contrib.graphviz
```

## Usage

Add graphviz to the extensions array in the
slide YAML header:

```markdown
---
title: A title
author: Me
date: 2019-12-04
extensions:
  - graphviz
---
```

With the extension installed and declared in the YAML header, use it in your
markdown like so:

~~~markdown
```graphviz

```
~~~
