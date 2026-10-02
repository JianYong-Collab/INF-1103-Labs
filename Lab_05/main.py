import data_manager
import io_manager

INVENTORY_FILE = "inventory.json"

data_manager.load_file(INVENTORY_FILE);
io_manager.display_menu()

