from ui.all_collections_view import AllCollectionsView
from ui.collection_view import CollectionView
from ui.login_view import LoginView
from ui.new_user_view import NewUserView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
        
    def start(self):
        self._show_login_view()
    
    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None
    
    def _show_login_view(self):
        self._hide_current_view()
        self._current_view = LoginView(self._root, self._show_new_user_view, self._show_all_collections_view)
        self._current_view.pack()
    
    def _show_new_user_view(self):
        self._hide_current_view()
        self._current_view = NewUserView(self._root, self._show_login_view)
        self._current_view.pack()
    
    def _show_all_collections_view(self):
        self._hide_current_view()
        self._current_view = AllCollectionsView(self._root, self._show_login_view, self._show_collection_view)
        self._current_view.pack()
    
    def _show_collection_view(self):
        self._hide_current_view()
        self._current_view = CollectionView(self._root, self._show_all_collections_view)
        self._current_view.pack()