from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
import time as waittime


class BasePage:

    def __init__(self, driver: WebDriver):
        """ Driver Instance"""
        self._driver = driver

    # Finding Elements
    def _find(self, locator: tuple) -> WebElement:
        """ find single element using locator"""
        return self._driver.find_element(*locator)

    def _find_elements(self, locator: tuple, time: int = 10) -> list:
        """ find multiple element instance using locator"""
        self._wait_until_presence_of_all_elements_located(locator, time)
        return self._driver.find_elements(*locator)

    # Clicking Element
    def _click(self, locator: tuple, time: int = 10) -> None:
        """ Clicking on the element"""
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    def _clickJS(self, locator: tuple, time: int = 10) -> None:
        """ Clicking on the element using JavaScript Click"""
        self._wait_until_element_is_clickable(locator, time)
        self._driver.execute_script("arguments[0].click()", self._find(locator))

    # Entering text in Input Fields
    def _type(self, locator: tuple, text: str, time: int = 10) -> None:
        """ Entering text into input field"""
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    # Clearing Text Box
    def _clear(self, locator: tuple, time: int = 10) -> None:
        """ Clearing the field"""
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).clear()
        waittime.sleep(2)

    # Expected Condition Waits
    def _wait_until_element_is_visible(self, locator: tuple, time: int = 10) -> None:
        try:
            wait = WebDriverWait(self._driver, time)
            wait.until(EC.visibility_of_element_located(locator))
        except Exception as error:
            print(f"Error: {error}")

    def _wait_until_element_is_clickable(self, locator: tuple, time: int = 10) -> None:
        try:
            wait = WebDriverWait(self._driver, time)
            wait.until(EC.element_to_be_clickable(locator))
        except Exception as error:
            print(f"Error: {error}")

    def _wait_until_element_to_be_selected(self, locator: tuple, time: int = 10) -> None:
        try:
            wait = WebDriverWait(self._driver, time)
            wait.until(EC.element_to_be_selected(locator))
        except Exception as error:
            print(f"Error: {error}")

    def _wait_until_invisibility_of_element_located(self, locator: tuple, time: int = 10) -> None:
        try:
            wait = WebDriverWait(self._driver, time)
            wait.until(EC.invisibility_of_element_located(locator))
        except Exception as error:
            print(f"Error: {error}")

    def _wait_until_presence_of_element_located(self, locator: tuple, time: int = 10) -> None:
        try:
            wait = WebDriverWait(self._driver, time)
            wait.until(EC.presence_of_element_located(locator))
        except Exception as error:
            print(f"Error: {error}")

    def _wait_until_text_to_be_present_in_element(self, locator: tuple, text: str, time: int = 10) -> None:
        try:
            wait = WebDriverWait(self._driver, time)
            wait.until(EC.text_to_be_present_in_element(locator, text))
        except Exception as error:
            print(f"Error: {error}")

    def _wait_until_title_contains(self, title: str, time: int = 10) -> bool:
        try:
            wait = WebDriverWait(self._driver, time)
            return wait.until(EC.title_contains(title))
        except Exception as error:
            print(f"Error: {error}")
            return False

    def _wait_until_title_is(self, title: str, time: int = 10) -> bool:
        try:
            wait = WebDriverWait(self._driver, time)
            return wait.until(EC.title_is(title))
        except Exception as error:
            print(f"Error: {error}")
            return False

    def _wait_until_visibility_of(self, locator: tuple, time: int = 10) -> WebElement:
        try:
            wait = WebDriverWait(self._driver, time)
            return wait.until(EC.visibility_of(locator))
        except Exception as error:
            print(f"Error: {error}")

    def _wait_until_presence_of_all_elements_located(self, locator: tuple, time: int = 10) -> WebElement:
        try:
            wait = WebDriverWait(self._driver, time)
            return wait.until(EC.presence_of_all_elements_located(locator))
        except Exception as error:
            print(f"Error: {error}")

    # Get Current URL
    @property
    def current_url(self) -> str:
        return self._driver.current_url

    # Is Displayed, enabled and Selected
    def _is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _is_enabled(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_enabled()
        except NoSuchElementException:
            return False

    def _is_selected(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_selected()
        except NoSuchElementException:
            return False

    # Launch URL
    def _open_url(self, url: str) -> None:
        self._driver.get(url)

    def _open_link_in_new_tab_get_attribute(self, locator: tuple, time: int = 10) -> None:
        source = WebDriverWait(self._driver, time).until(EC.presence_of_element_located(locator))
        url = source.get_attribute("href")
        self._driver.execute_script(f"window.open('{url}');")

    # Extracting Methods
    def _get_text(self, locator: tuple, time: int = 10) -> str:
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).text

    def _get_page_source(self) -> str:
        return self._driver.page_source

    def _get_title(self) -> str:
        return self._driver.title

    def _get_attribute_value(self, locator: tuple, attributename: str, time: int = 10) -> str:
        source = WebDriverWait(self._driver, time).until(EC.presence_of_element_located(locator))
        return source.get_attribute(attributename)

    def _get_element_count(self, locator: tuple, time: int = 10) -> int:
        source = WebDriverWait(self._driver, time).until(EC.presence_of_all_elements_located(locator))
        return len(self._find_elements(source))

    # Drop down methods
    def _get_drp_dwn_opts(self, locator: tuple, option_value_by_text: bool = False, time: int = 10) -> list:
        self._wait_until_element_is_visible(locator, time)
        element = self._find(locator)
        all_options = element.find_elements(By.TAG_NAME, "option")
        return [option.text if option_value_by_text else option.get_attribute('value') for option in all_options]

    def _drp_dwn_slt_by_index(self, locator: tuple, index: int) -> None:
        select = Select(self._find(locator))
        select.select_by_index(index)

    def _drp_dwn_slt_by_visible_txt(self, locator: tuple, text: str) -> None:
        select = Select(self._find(locator))
        select.select_by_visible_text(text)

    def _drp_dwn_slt_by_value(self, locator: tuple, value: str) -> None:
        select = Select(self._find(locator))
        select.select_by_value(value)

    def _drp_dwn_deselectall(self, locator: tuple) -> None:
        """Only valid when the drop-down element supports multiple selections."""
        select = Select(self._find(locator))
        select.deselect_all()

    def _drp_dwn_get_all_options(self, locator: tuple) -> list:
        select = Select(self._find(locator))
        return [data.text for data in select.options]

    # Drag and Drop
    def _drag_and_drop_element_from_source_to_target(self, source: tuple, target: tuple) -> None:
        action_chains = ActionChains(self._driver)
        action_chains.drag_and_drop(self._find(source), self._find(target)).perform()

    def _drag_and_drop_clk_hld_move_to_element(self, source: tuple, target: tuple) -> None:
        action_chains = ActionChains(self._driver)
        action_chains.click_and_hold(self._find(source)).pause(2).move_to_element(self._find(target)).perform()

    # Mouse Action
    def _mouse_double_click_at_source(self, locator: tuple, time: int = 10) -> None:
        source = WebDriverWait(self._driver, time).until(EC.presence_of_element_located(locator))
        action = ActionChains(self._driver)
        action.double_click(source).perform()

    def _mouse_context_click_at_source(self, locator: tuple, time: int = 10) -> None:
        source = WebDriverWait(self._driver, time).until(EC.presence_of_element_located(locator))
        action = ActionChains(self._driver)
        action.context_click(source).perform()

    def _mouse_hover_at_source(self, locator: tuple, time: int = 10) -> None:
        source = WebDriverWait(self._driver, time).until(EC.presence_of_element_located(locator))
        action = ActionChains(self._driver)
        action.move_to_element(source).perform()

    # Windows Handle
    def _get_current_window_address(self) -> str:
        return self._driver.current_window_handle

    def _get_browser_name(self) -> str:
        return self._driver.name

    def _get_all_window_addresses(self) -> list:
        return self._driver.window_handles

    def _switch_to_window(self, window_address: str) -> None:
        self._driver.switch_to.window(window_address)

    # Frame Handling
    def _switch_to_default_content(self) -> None:
        self._driver.switch_to.default_content()

    def _switch_to_frame_by_name_or_id_attribute(self, name_attribute: str) -> None:
        self._driver.switch_to.frame(name_attribute)

    def _switch_to_parent_frame(self) -> None:
        self._driver.switch_to.parent_frame()

    def _switch_to_frame_using_locator(self, locator: tuple) -> None:
        self._driver.switch_to.frame(self._find(locator))

    # Alert Handling
    def _alert_reference(self) -> Alert:
        alert = Alert(self._driver)
        return alert

    def _alert_accept(self, extract_text: bool = False) -> str:
        alert_text = None
        reference = self._alert_reference()
        if extract_text:
            alert_text = reference.text
        reference.accept()
        return alert_text

    def _alert_dismiss(self, extract_text: bool = False) -> str:
        alert_text = None
        reference = self._alert_reference()
        if extract_text:
            alert_text = reference.text
        reference.dismiss()
        return alert_text

    def _alert_prompt_field(self, type_text: str = "test", extract_text: bool = False) -> str:
        alert_text = None
        reference = self._alert_reference()
        reference.send_keys(type_text)
        if extract_text:
            alert_text = reference.text
        return alert_text

    # Browser Navigation
    def _navigate_forward(self) -> None:
        self._driver.forward()

    def _navigate_backward(self) -> None:
        self._driver.back()

    def _close_current_window(self) -> None:
        self._driver.close()

    def _current_page_refresh(self) -> None:
        self._driver.refresh()

    # Cookies Handling
    def _set_cookies(self, dict_data: dict) -> None:
        self._driver.add_cookie(dict_data)

    def _get_cookies(self) -> list[dict]:
        return self._driver.get_cookies()

    def _get_cookie_by_name(self, name: str) -> dict | None:
        return self._driver.get_cookie(name)

    def _delete_all_cookies(self) -> None:
        self._driver.delete_all_cookies()

    def _delete_cookie_by_name(self, name: str) -> None:
        self._driver.delete_cookie(name)

    # Element Modification
    def _update_attribute_value(self, locator: tuple, attributeName: str, attributeValue: str, time: int = 10) -> None:
        source = WebDriverWait(self._driver, time).until(EC.presence_of_element_located(locator))
        self._driver.execute_script("arguments[0].setAttribute(arguments[1], arguments[2]);", source,
                                    attributeName, attributeValue)
