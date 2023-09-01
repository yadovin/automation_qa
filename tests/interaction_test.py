from pages.interactions_page import SortablePage
from conftest import driver


class TestInteractions:
    class TestSortablePage:

        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            list_before,list_after = sortable_page.change_list_order()
            grid_before,grid_after = sortable_page.change_gride_order()
            assert list_after != list_before, 'order of the list has not been changed'
            assert grid_after != grid_before, 'order of the grid has not been changed'


