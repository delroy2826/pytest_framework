from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time as waittime


class BasePage:

    def __init__(self, driver: WebDriver):
        """ Driver Instance"""
        self._driver = driver

    # Finding Elements
    def _find(self, locator: tuple) -> WebElement:
        """
        Finds single element using locator
        :param locator: Element Identifier
        :return: Returns WebElement
        """
        return self._driver.find_element(*locator)

    def _find_elements(self, locator: tuple, time: int = 10) -> list:
        """
        Find multiple element instance using locator
        :param locator: Element Identifier
        :param time: Time in Seconds
        :return: Returns list of WebElement
        """
        self._wait_until_presence_of_all_elements_located(locator, time)
        return self._driver.find_elements(*locator)

    # Clicking Element
    def _click(self, locator: tuple, time: int = 10) -> None:
        """
        Clicking on the element
        :param locator: Element Identifier
        :param time: Time in Seconds
        """
        instance = self._wait_until_element_is_clickable(locator, time)
        instance.click()

    def _clickJS(self, locator: tuple, time: int = 10) -> None:
        """
        Clicking on the element using JavaScript Click
        :param locator: Element Identifier
        :param time: Time in Seconds
        """
        instance = self._wait_until_element_is_clickable(locator, time)
        self._driver.execute_script("arguments[0].click()", instance)

    # Entering text in Input Fields
    def _type(self, locator: tuple, text: str, time: int = 10) -> None:
        """
        Entering text into input field
        :param locator: Element Identifier
        :param text: Text to be entered in the input field
        :param time: Time in Seconds
        """
        instance = self._wait_until_element_is_visible(locator, time)
        if instance:
            instance.send_keys(text)
        else:
            print(f"Failed function '_type' for {instance}")

    # Clearing Text Box
    def _clear(self, locator: tuple, time: int = 10) -> None:
        """
        Clearing the field
        :param locator: Element Identifier
        :param time: Time in Seconds
        """
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).clear()
        waittime.sleep(2)

    # Expected Condition Waits
    def _wait_until_element_is_visible(self, locator: tuple, time: int = 10) -> WebElement | bool:
        """
        Waits until element is visible
        :param locator: Element Identifier
        :param time: Time in Seconds
        :return:
        """
        try:
            wait = WebDriverWait(self._driver, time)
            return wait.until(EC.visibility_of_element_located(locator))
        except Exception as error:
            raise Exception(f"Error: {error}")

    def _wait_until_element_is_clickable(self, locator: tuple, time: int = 10) -> WebElement:
        """
        Waits until element is clickable
        :param locator: Element Identifier
        :param time: Time in Seconds
        :return:
        """
        try:
            wait = WebDriverWait(self._driver, time)
            return wait.until(EC.element_to_be_clickable(locator))
        except Exception as error:
            print(f"Error: {error}")

    def _wait_until_element_to_be_selected(self, locator: tuple, time: int = 10) -> None:
        """
        Waits until element to be selected
        :param locator: Element Identifier
        :param time: Time in Seconds
        :return:
        """
        try:
            wait = WebDriverWait(self._driver, time)
            wait.until(EC.element_to_be_selected(locator))
        except Exception as error:
            print(f"Error: {error}")

    def _wait_until_invisibility_of_element_located(self, locator: tuple, time: int = 10) -> None:
        """
        Waits until element is invisible
        :param locator: Element Identifier
        :param time: Time in Seconds
        :return:
        """
        try:
            wait = WebDriverWait(self._driver, time)
            wait.until(EC.invisibility_of_element_located(locator))
        except Exception as error:
            print(f"Error: {error}")

    def _wait_until_presence_of_element_located(self, locator: tuple, time: int = 10) -> None:
        """
        Waits until element is presence
        :param locator: Element Identifier
        :param time: Time in Seconds
        :return:
        """
        try:
            wait = WebDriverWait(self._driver, time)
            wait.until(EC.presence_of_element_located(locator))
        except Exception as error:
            print(f"Error: {error}")

    def _wait_until_text_to_be_present_in_element(self, locator: tuple, text: str, time: int = 10) -> None:
        """
        Waits until element is having expected text
        :param locator: Element Identifier
        :param text: Text to be present
        :param time: Time in Seconds
        :return:
        """
        try:
            wait = WebDriverWait(self._driver, time)
            wait.until(EC.text_to_be_present_in_element(locator, text))
        except Exception as error:
            print(f"Error: {error}")

    def _wait_until_title_contains(self, title: str, time: int = 10) -> bool:
        """
        Waits for the title contains expected title
        :param title: Expected title text
        :param time: Time in Seconds
        :return: Returns True or False
        """
        try:
            wait = WebDriverWait(self._driver, time)
            return wait.until(EC.title_contains(title))
        except Exception as error:
            print(f"Error: {error}")
            return False

    def _wait_until_title_is(self, title: str, time: int = 10) -> bool:
        """
        Waits until title is equal to expected title
        :param title: Expected Title
        :param time: Time in Seconds
        :return: Returns True or False
        """
        try:
            wait = WebDriverWait(self._driver, time)
            return wait.until(EC.title_is(title))
        except Exception as error:
            print(f"Error: {error}")
            return False

    def _wait_until_visibility_of(self, locator: tuple, time: int = 10) -> WebElement:
        """
        Waits until visibility of element located
        :param locator: Element Identifier
        :param time: Time in Seconds
        :return: Returns WebElement
        """
        try:
            wait = WebDriverWait(self._driver, time)
            return wait.until(EC.visibility_of(locator))
        except Exception as error:
            print(f"Error: {error}")

    def _wait_until_presence_of_all_elements_located(self, locator: tuple, time: int = 10) -> WebElement:
        """
        Waits until elements are located
        :param locator: Element Identifier
        :param time: Time in Seconds
        :return: Returns WebElement
        """
        try:
            wait = WebDriverWait(self._driver, time)
            return wait.until(EC.presence_of_all_elements_located(locator))
        except Exception as error:
            print(f"Error: {error}")

    # Get Current URL
    @property
    def current_url(self) -> str:
        """
        Gets current URL
        :return: Returns string
        """
        return self._driver.current_url

    # Is Displayed, enabled and Selected
    def _is_displayed(self, locator: tuple, time: int = 10) -> bool:
        """
        Checks if Element is Displayed
        :param locator: Element Identifier
        :return: Returns True or False
        """
        try:
            instance = self._wait_until_element_is_visible(locator, time)
            return instance.is_displayed()
        except Exception as error:
            print(error)
            return False

    def _is_enabled(self, locator: tuple) -> bool:
        """
        Checks if button is enabled
        :param locator: Element Identifier
        :return: Return True or False
        """
        try:
            return self._find(locator).is_enabled()
        except NoSuchElementException:
            return False

    def _is_selected(self, locator: tuple) -> bool:
        """
        Checks if the checkbox or round button is selected
        :param locator: Element Identifier
        :return: Return True or False
        """
        try:
            return self._find(locator).is_selected()
        except NoSuchElementException:
            return False

    # Launch URL
    def _open_url(self, url: str) -> None:
        """
        Opens URL in the browser
        :param url: Expected URL to be launched
        """
        self._driver.get(url)

    def _open_link_in_new_tab_get_attribute(self, locator: tuple, time: int = 10) -> None:
        """
        Extracts href value from tag and opens the url in new tab
        :param locator: Element Identifier
        :param time: Time in Seconds
        """
        source = WebDriverWait(self._driver, time).until(EC.presence_of_element_located(locator))
        url = source.get_attribute("href")
        self._driver.execute_script(f"window.open('{url}');")

    # Extracting Methods
    def _get_text(self, locator: tuple, time: int = 10) -> str:
        """
        Extracts text from the element
        :param locator: Element Identifier
        :param time: Time in Seconds
        :return: Return String
        """
        instance = self._wait_until_element_is_visible(locator, time)
        return instance.text

    def _get_page_source(self) -> str:
        """
        Extracts page source code
        :return: Returns string
        """
        return self._driver.page_source

    def _get_title(self) -> str:
        """
        Extracts Title
        :return: Returns String
        """
        return self._driver.title

    def _get_attribute_value(self, locator: tuple, attributename: str, time: int = 10) -> str:
        """
        Extracts tag attribute value
        :param locator: Element Identifier
        :param attributename: attribute name
        :param time: Time in Seconds
        :return: Returns String
        """
        source = WebDriverWait(self._driver, time).until(EC.presence_of_element_located(locator))
        return source.get_attribute(attributename)

    def _get_element_count(self, locator: tuple, time: int = 10) -> int:
        """
        Returns total count of elements found in the page
        :param locator: Element Identifier
        :param time: Time in Seconds
        :return: Returns Integer
        """
        source = WebDriverWait(self._driver, time).until(EC.presence_of_all_elements_located(locator))
        return len(self._find_elements(source))

    # Drop down methods
    def _get_drp_dwn_opts(self, locator: tuple, option_value_by_text: bool = False, time: int = 10) -> list:
        """
        Returns List of options available in the drop down
        :param locator: Element Identifier
        :param option_value_by_text: If you want to extract text then value will be True else False
        :param time: Time in Seconds
        :return: Returns List
        """
        self._wait_until_element_is_visible(locator, time)
        element = self._find(locator)
        all_options = element.find_elements(By.TAG_NAME, "option")
        return [option.text if option_value_by_text else option.get_attribute('value') for option in all_options]

    def _drp_dwn_slt_by_index(self, locator: tuple, index: int) -> None:
        """
        Selects drop down option by Index
        :param locator: Element Identifier
        :param index: Index number
        """
        select = Select(self._find(locator))
        select.select_by_index(index)

    def _drp_dwn_slt_by_visible_txt(self, locator: tuple, text: str) -> None:
        """
        Selects drop down option by text
        :param locator: Element Identifier
        :param text: Text to be selected in the option
        """
        select = Select(self._find(locator))
        select.select_by_visible_text(text)

    def _drp_dwn_slt_by_value(self, locator: tuple, value: str) -> None:
        """
        Selects the drop down option by value
        :param locator: Element Identifier
        :param value: Value to be selected from drop down
        """
        select = Select(self._find(locator))
        select.select_by_value(value)

    def _drp_dwn_deselectall(self, locator: tuple) -> None:
        """
        Only valid when the drop-down element supports multiple selections.
        :param locator: Element Identifier
        """
        select = Select(self._find(locator))
        select.deselect_all()

    def _drp_dwn_get_all_options(self, locator: tuple) -> list:
        """
        Gets all options text of the drop down
        :param locator: Element Identifier
        :return: Return List of Extracted values
        """
        select = Select(self._find(locator))
        return [data.text for data in select.options]

    # Drag and Drop
    def _drag_and_drop_element_from_source_to_target(self, source: tuple, target: tuple) -> None:
        """
        Drags and Drops element from Source to target
        :param source: Element to be dragged
        :param target: Location where the dragged element to be dropped
        """
        action_chains = ActionChains(self._driver)
        action_chains.drag_and_drop(self._find(source), self._find(target)).perform()

    def _drag_and_drop_clk_hld_move_to_element(self, source: tuple, target: tuple) -> None:
        """
        Drags and Drops by Click hold
        :param source: Element to be Clicked and Hold
        :param target: Location where the Hold element to be released
        """
        action_chains = ActionChains(self._driver)
        action_chains.click_and_hold(self._find(source)).pause(2).move_to_element(self._find(target)).perform()

    # Mouse Action
    def _mouse_double_click_at_source(self, locator: tuple, time: int = 10) -> None:
        """
        Mouse Double Click
        :param locator: Element Identifier
        :param time: Time in Seconds
        """
        source = WebDriverWait(self._driver, time).until(EC.presence_of_element_located(locator))
        action = ActionChains(self._driver)
        action.double_click(source).perform()

    def _mouse_context_click_at_source(self, locator: tuple, time: int = 10) -> None:
        """
        Right Click in Mouse
        :param locator: Element Identifier
        :param time: Time in SecondS
        """
        source = WebDriverWait(self._driver, time).until(EC.presence_of_element_located(locator))
        action = ActionChains(self._driver)
        action.context_click(source).perform()

    def _mouse_hover_at_source(self, locator: tuple, time: int = 10) -> None:
        """
        Hoevers mouse pointer on top of element
        :param locator: Element Identifier
        :param time: Time in Seconds
        """
        source = WebDriverWait(self._driver, time).until(EC.presence_of_element_located(locator))
        action = ActionChains(self._driver)
        action.move_to_element(source).perform()

    # Windows Handle
    def _get_current_window_address(self) -> str:
        """
        Returns current window address
        :return: Returns String
        """
        return self._driver.current_window_handle

    def _get_browser_name(self) -> str:
        """
        Gets browser name
        :return:  Returns String
        """
        return self._driver.name

    def _get_all_window_addresses(self) -> list:
        """
        Returns list of window addresses
        :return: Returns List of window addresses
        """
        return self._driver.window_handles

    def _switch_to_window(self, window_address: str) -> None:
        """
        Switch's to new window using address
        :param window_address: Window address to be switched
        """
        self._driver.switch_to.window(window_address)

    # Frame Handling
    def _switch_to_default_content(self) -> None:
        """
        Switches to default content
        """
        self._driver.switch_to.default_content()

    def _switch_to_frame_by_name_or_id_attribute(self, name_attribute: str) -> None:
        """
        Switches to frame by name or id attribute
        :param name_attribute: name attribute value
        """
        self._driver.switch_to.frame(name_attribute)

    def _switch_to_parent_frame(self) -> None:
        """
        Switches to parent frame
        """
        self._driver.switch_to.parent_frame()

    def _switch_to_frame_using_locator(self, locator: tuple) -> None:
        """
        Switches to frame using Locator
        :param locator: Element Identifier
        """
        self._driver.switch_to.frame(self._find(locator))

    # Alert Handling
    def _alert_reference(self) -> Alert:
        """
        Instance generator for Alert
        :return: Return Alert Object reference
        """
        alert = Alert(self._driver)
        return alert

    def _alert_accept(self, extract_text: bool = False) -> str | None:
        """
        Accepts alert prompt and extracts text as per requirement
        :param extract_text: Extracts text based on True or False
        :return: Returns String
        """
        alert_text = None
        reference = self._alert_reference()
        if extract_text:
            alert_text = reference.text
        reference.accept()
        return alert_text

    def _alert_dismiss(self, extract_text: bool = False) -> str | None:
        """
        Dismisses alert prompt and extracts text as per requirement
        :param extract_text: Extracts text based on True or False
        :return: Returns String
        """
        alert_text = None
        reference = self._alert_reference()
        if extract_text:
            alert_text = reference.text
        reference.dismiss()
        return alert_text

    def _alert_prompt_field(self, type_text: str = "test", extract_text: bool = False) -> str | None:
        """
        Enters text in the field and extracts text as per requirement
        :param type_text: Text to be entered in the alert input box
        :param extract_text: Extracts text based on True or False
        :return: Returns String
        """
        alert_text = None
        reference = self._alert_reference()
        reference.send_keys(type_text)
        if extract_text:
            alert_text = reference.text
        return alert_text

    # Browser Navigation
    def _navigate_forward(self) -> None:
        """
        Navigates to forward page
        """
        self._driver.forward()

    def _navigate_backward(self) -> None:
        """
        Navigates to previous page
        """
        self._driver.back()

    def _close_current_window(self) -> None:
        """
        Closes the current window or tab of the browser
        """
        self._driver.close()

    def _current_page_refresh(self) -> None:
        """
        Refresh the web page
        """
        self._driver.refresh()

    # Cookies Handling
    def _set_cookies(self, dict_data: dict) -> None:
        """
        Adds cookies using dictionary
        :param dict_data: dictionary data with key and value
        """
        self._driver.add_cookie(dict_data)

    def _get_cookies(self) -> list[dict]:
        """
        Extracts all cookies
        :return: Returns list of dictionary
        """
        return self._driver.get_cookies()

    def _get_cookie_by_name(self, name: str) -> dict | None:
        """
        Extracts cookies by name
        :param name: Name is the key
        :return:
        """
        return self._driver.get_cookie(name)

    def _delete_all_cookies(self) -> None:
        """
        Deletes all cookies
        """
        self._driver.delete_all_cookies()

    def _delete_cookie_by_name(self, name: str) -> None:
        """
        Deletes the cookie by name
        :param name: Name is the key
        :return:
        """
        self._driver.delete_cookie(name)

    # Element Modification
    def _update_attribute_value(self, locator: tuple, attributeName: str, attributeValue: str, time: int = 10) -> None:
        """
        Update tag attribute and attribute value
        :param locator: Element Identifier
        :param attributeName: Attribute name
        :param attributeValue: Attribute value
        :param time: Time in Seconds
        """
        source = WebDriverWait(self._driver, time).until(EC.presence_of_element_located(locator))
        self._driver.execute_script("arguments[0].setAttribute(arguments[1], arguments[2]);", source,
                                    attributeName, attributeValue)

    # Scrolling
    def _scroll_to_element(self, locator: tuple, time: int = 10) -> None:
        """
        Scroll to the defined element
        :param locator: Element Identifier
        :param time: Time in Seconds
        """
        source = WebDriverWait(self._driver, time).until(EC.presence_of_element_located(locator))
        action_chains = ActionChains(self._driver)
        action_chains.scroll_to_element(source).perform()

    def _scroll_by_amount(self, delta_x: int = 0, delta_y: int = 0, time: int = 10) -> None:
        """
        Scrolls the page using provided attributes delta_x and delta_y
        :param delta_x: Distance along X axis to scroll using the wheel. A negative value scrolls left.
        :param delta_y: Distance along Y axis to scroll using the wheel. A negative value scrolls up.
        :param time: Time in Seconds
        """
        counter = 0
        while counter < time + 1:
            status = self._driver.execute_script("return document.readyState")
            if status in ("complete", "interactive"):
                break
            counter += 1
        action_chains = ActionChains(self._driver)
        action_chains.scroll_by_amount(delta_x, delta_y).perform()

    def _scroll_by_origin_by_element(self, locator: tuple, delta_x: int = 0, delta_y: int = 0, time: int = 10) -> None:
        """
        Scrolls the page from the element location to provided delta_x and delta_y
        origin: Where scroll originates (viewport or element center) plus provided offsets.
        :param locator: Element Identifier
        :param delta_x: Distance along X axis to scroll using the wheel. A negative value scrolls left.
        :param delta_y: Distance along Y axis to scroll using the wheel. A negative value scrolls up.
        :param time: Time in Seconds
        """
        source = WebDriverWait(self._driver, time).until(EC.presence_of_element_located(locator))
        scroll_origin = ScrollOrigin.from_element(source)
        counter = 0
        while counter < time + 1:
            status = self._driver.execute_script("return document.readyState")
            if status in ("complete", "interactive"):
                break
            counter += 1
        action_chains = ActionChains(self._driver)
        action_chains.scroll_from_origin(scroll_origin, delta_x, delta_y).perform()

    def _scroll_by_js(self, delta_x: int = 0, delta_y: int = 0, time: int = 10) -> None:
        """
        Scrolls by JavaScript
        :param delta_x: Distance along X axis to scroll using the wheel. A negative value scrolls left.
        :param delta_y: Distance along Y axis to scroll using the wheel. A negative value scrolls up.
        :param time: Time in Seconds
        """
        counter = 0
        while counter < time + 1:
            status = self._driver.execute_script("return document.readyState")
            if status in ("complete", "interactive"):
                break
            counter += 1
        self._driver.execute_script(f"window.scrollBy({delta_x},{delta_y})")

    def _scroll_into_view_js(self, locator: tuple, time: int = 10) -> None:
        """
        Scrolling to element using locator
        :param locator: Element Identifier
        :param time: Time in Seconds
        """
        source = WebDriverWait(self._driver, time).until(EC.presence_of_element_located(locator))
        self._driver.execute_script("arguments[0].scrollIntoView();", source)

    def _return_page_height(self) -> int:
        """
        Returns total height of the page
        :return: Returns integer
        """
        total_height = self._driver.execute_script("return document.body.parentNode.scrollHeight")
        return total_height

    def _scroll_to_end_of_page(self, time: int = 10):
        """
        Scroll to end of the page
        :param time: Time in Seconds
        """
        counter = 0
        while counter < time + 1:
            status = self._driver.execute_script("return document.readyState")
            if status in ("complete", "interactive"):
                break
            counter += 1
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    @staticmethod
    def _positional_arg_locator(locator: tuple, *args) -> tuple:
        """
        Replaces arguments in locator element
        :param locator: locator tuple passed
        :param args: data or values to be inserted in locator str using string formatting
        :return: return tuple
        """
        cp_locator = list(locator)
        cp_locator[1] = cp_locator[1].format(*args)
        return tuple(cp_locator)
