from talon import Context, Module, actions, app

mod = Module()
ctx = Context()


@mod.action_class
class Actions:
    def rotate_word(word_to_rotate: str):
        """Rotate word"""
        # TODO: support case preserving rotation
        candidates = []
        homophones = actions.user.homophones_get_all()
        candidates = homophones.get(word_to_rotate)

        if not candidates:
            app.notify("no candidates found")
            return

        actions.edit.select_all()
        text = actions.edit.selected_text()
        words = text.split()

        for candidate in candidates:
            if candidate not in words:
                continue

            old_index = homophones[candidate].index(candidate)
            new_index = (old_index + 1) % len(homophones[candidate])
            replacement = homophones[candidate][new_index]
            new_text = text.replace(candidate, replacement)

            actions.user.paste(new_text)
