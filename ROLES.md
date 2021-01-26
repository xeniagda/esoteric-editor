# Roles (Pseudo-randomly assigned)
When a certain portion is completed here, please mark it as completed here, along with the language it was done in.

Assignees are given under each heading. There can be multiple assignees per section if needed, and you can ask for appointment to multiple sections.

You may add more tasks if deemed necessary.

## TUI
@sinthorion
- [ ] text rendering
- [ ] header
- [ ] footer
- [ ] scroll bars
## GUI
@razetime
- [ ] window, pixel buffer management
- [ ] text rendering
- [ ] gpu acceleration<sup>*</sup>
## File I/O (new, open, save)
@kspalaiologos
- [ ] remote editing?
- [ ] file search maybe?
- [ ] file type recognition
## Actual Text Editing
@loovjo
- [ ] simple editing operations (undo, redo, copy) *Note:* lots of things can be stolen from kakoune, vim, emacs etc to put here
- [ ] multiple cursors
- [ ] shortcuts
## Navigation
- [ ] jump to definition, declaration etc.
- [ ] see usages of thing
- [ ] literal search
## State Manager/Glue (to hold the editor state and broadcast it to different components)
@ubq323
- [ ] modal based editing<sup>*</sup>
## Formatting<sup>*</sup>
- [ ] maybe simple semantic "parsing" (locate definitions, etc)
- [ ] a way to find what indentation the current file is using (tabs, 4 spaces, 2 spaces etc)
## Scripting API
@FireCubez
 - [ ] command parser
 - [ ] some script lang for the editor
## Testing
@Anima Libera

<sup>*</sup>: Indicates an idea that is in flux, and may be discarded.