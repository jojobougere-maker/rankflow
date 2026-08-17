class PageRouter:
    """Route sidebar actions to persistent in-window page views."""

    def __init__(self, buttons):
        self.buttons = buttons
        self.pages = {}
        self.active_page = None

    def register(self, name, page):
        self.pages[name] = page
        page.grid(row=0, column=0, sticky="nsew")
        page.grid_remove()
        self.buttons[name].configure(command=lambda page_name=name: self.show(page_name))

    def show(self, name):
        if name == self.active_page or name not in self.pages:
            return

        if self.active_page:
            self.pages[self.active_page].grid_remove()

        page = self.pages[name]
        page.grid()
        page.after_idle(page.tkraise)
        self._set_active_button(name)
        self.active_page = name

    def _set_active_button(self, active_name):
        for name, button in self.buttons.items():
            button.configure(fg_color="#7C5CFF" if name == active_name else "transparent")
