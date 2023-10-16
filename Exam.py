class MenuItem:
    def __init__(self, id, name, parent_id):
        self.id = id
        self.name = name
        self.parent_id = parent_id
        self.children = []

class MenuBuilder:
    def __init__(self, path):
        self.menu_items = self.load_menu_items(path)
        self.menu = self.build_menu()

    def load_menu_items(self, path):
        menu_items = {}
        with open(path, 'r', encoding="utf-8") as file:
            for line in file:
                id, name, parent_id = line.strip().split(',')
                menu_items[int(id)] = MenuItem(int(id), name, int(parent_id))
        return menu_items

    def build_menu(self):
        root = None
        for item in self.menu_items.values():
            if item.parent_id == 0:
                root = item
            else:
                parent = self.menu_items.get(item.parent_id)
                if parent:
                    parent.children.append(item)
        return root

    def display_menu(self, item=None, prefix=''):
        if item is None:
            item = self.menu
        print(f'{prefix}{item.name}')
        for child in item.children:
            self.display_menu(child, prefix + '  • ')

    def get_path(self, menu_item, target):
        if menu_item.id == target.id or menu_item.name == target.name:
            return [menu_item.name]
        for child in menu_item.children:
            path = self.get_path(child, target)
            if path is not None:
                return [menu_item.name] + path
        return None

builder = MenuBuilder('menu_items.txt')
builder.display_menu()
while True:
    target_name_or_id = input('Введите id/Название пункта: ')
    if target_name_or_id.isdigit():
        target = builder.menu_items.get(int(target_name_or_id))
    else:
        target = next((item for item in builder.menu_items.values() if item.name == target_name_or_id), None)
    if target is not None:
        path = builder.get_path(builder.menu, target)
        print('Цепочка пунктов: ' + ' -> '.join(path))
    else:
        print('Пункт меню не найден.')