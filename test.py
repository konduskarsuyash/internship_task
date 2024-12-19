from playwright.sync_api import sync_playwright

def run_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  
        page = browser.new_page()

        page.goto('https://www.google.com')

        page.fill('textarea[name="q"]', 'Hans Zimmer')  
        page.press('textarea[name="q"]', 'Enter')

        page.wait_for_selector('h3')

        first_link = page.query_selector('h3')
        first_link.click()

        page.wait_for_load_state('domcontentloaded')
        page_content = page.inner_text('body')
        
        h1_content = page.inner_text('h1#firstHeading.firstHeading')
        print("Extracted H1 content:", h1_content)

        print(page_content)

        browser.close()

if __name__ == "__main__":
    run_test()
