from django.contrib.auth import get_user_model
from .base import FunctionalTest
from .my_lists_page import MyListsPage
from .list_page import ListPage


User = get_user_model()

class MyListsTest(FunctionalTest):

    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        # Edith is a logged-in user
        self.create_pre_authenticated_session('edith@example.com')

        # She goes to the home page and start a list
        self.browser.get(self.live_server_url)
        ListPage(self).add_list_item('Reticulate splines')
        ListPage(self).add_list_item('Immanentize eschaton')
        first_list_url = self.browser.current_url

        # She notices a "My lists" link, for the first time.
        MyListsPage(self).go_to_my_lists_page()

        # She sees that her list is in there, named according to its
        # first list item
        self.wait_for(
            lambda: self.browser.find_element_by_link_text('Reticulate splines')
        )
        self.browser.find_element_by_link_text('Reticulate splines').click()
        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, first_list_url)
        )

        # She decides to start another list, just to see
        self.browser.get(self.live_server_url)
        ListPage(self).add_list_item('Click cows')
        second_list_url = self.browser.current_url

        # Under "my lists", her new list appears
        MyListsPage(self).go_to_my_lists_page()
        self.wait_for(
            lambda: self.browser.find_element_by_link_text('Click cows')
        )
        self.browser.find_element_by_link_text('Click cows').click()
        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, second_list_url)
        )

        # She go back to "my lists" page, There is a "delete" button on the right side of each list
        MyListsPage(self).go_to_my_lists_page()
        my_lists_url = self.browser.current_url
        self.wait_for(
            lambda: self.browser.find_element_by_id('Click cows')
        )
        # selected_list = self.browser.find_element_by_link_text('Click cows')
        selected_list_item = self.browser.find_element_by_id('Click cows')

        # After she clicked it, page refresh and the list disappeared
        selected_list_item.find_element_by_tag_name("button").click()
        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, my_lists_url)
        )
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Click cows', page_text)


        # She logs out. The "My lists" option disappears
        self.browser.find_element_by_link_text('Log out').click()
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_elements_by_link_text('My lists'),
            []
        ))