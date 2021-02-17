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
      -> text rendering
      -> header, footer, scroll bars etc rendering
    -> gui
      -> window, pixel buffer management
      -> text rendering
      -> gpu acceleration ???
      -> ????
  -> logic
    -> file i/o (new, open, save)
      -> remote editing?
      -> file search maybe?
      -> file type recognition
    -> editing operations (undo, redo, copy)
      * lots of things can be stolen from kakoune, vim, emacs etc to put here
    -> navigation
      -> jump to definition, declaration etc.
      -> see usages of thing
      -> literal search
    -> state manager (to hold the editor state and broadcast it to different components)
      -> modal editor???
    -> syntax highlighting
      -> maybe simple semantic "parsing" (locate definitions, etc)
    -> indentation
      -> a way to find what the current file is using (tabs, 4 spaces, 2 spaces etc)
    -> scripting
       -> command parser
       -> some script lang for the editor
```

## Interested in Compiling/Optimizing?
Even better! We want this editor to be usable after all. As we choose ~~weird~~ totally reasonable languages, we'll need to make sure the editor still runs. And that's where you come in!
