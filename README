# Esoteric Editor
Have you ever looked at popular text editors, thought, "These are all so sensible! I can't use an editor written in only one programming language!" and ended up toggling the bits by hand? We're here to help, with a text editor made in so many languages it'll make your eyes water.

## How many languages, you say?
Many, hopefully. We aim to have no language overlap between any components of the editor, and we have a penchant for less common programming languages. If you've heard of Brainfuck, you know what to expect.

## That sounds wonderful! Where can I download it?
I admire your enthusiasm, but alas, it's not made yet. Maybe you can channel that enthusiasm into helping us achieve our dream. When it's usable, you'll be able to download a Docker image to assemble the horde of dependencies.

## Helping out? Sign me up!
Great, here's the battle plan:
```
editor
  -> view
    -> tui
    -> gui
  -> logic
    -> file i/o (new, open, save)
    -> editing operations (undo, redo, copy)
    -> state manager (to hold the editor state and broadcast it to different components)
       -> protocol support for different components
    -> syntax highlighting
    -> indentation
    -> scripting
       -> command parser
       -> some script lang for the editor
```
