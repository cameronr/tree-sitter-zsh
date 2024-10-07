# tree-sitter-zsh

[![CI][ci]](https://github.com/tree-sitter/tree-sitter-zsh/actions/workflows/ci.yml)
[![discord][discord]](https://discord.gg/w7nTvsVJhm)
[![matrix][matrix]](https://matrix.to/#/#tree-sitter-chat:matrix.org)

<!--[![crates][crates]](https://crates.io/crates/tree-sitter-zsh)-->
<!--[![npm][npm]](https://www.npmjs.com/package/tree-sitter-zsh)-->
<!--[![pypi][pypi]](https://pypi.org/project/tree-sitter-zsh)-->

Experimental Zsh grammar for [tree-sitter](https://github.com/tree-sitter/tree-sitter).

This is an "experiemental" fork of the [Bash grammar](https://github.com/tree-sitter/tree-sitter-bash).

I don't know what I'm doing. It's probably not correct and probably doesn't do what you want.

## Development

Building the parser:

```sh
gmake
```

Running tree-sitter tests:

```sh
gmake test
```

For using the playground:

```sh
npm install
```

Build and run the playround

```sh
npm run start
```

Run the node tests

```sh
npm run test
```

### References

- [Bash grammar](https://github.com/tree-sitter/tree-sitter-bash).
- [Zsh Shell Grammar](https://zsh.sourceforge.io/Doc/Release/Shell-Grammar.html#Shell-Grammar)
