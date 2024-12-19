from playwright.sync_api import sync_playwright

def run_test():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)  # Set headless=False to see the browser
        page = browser.new_page()

        # Navigate to google.com
        page.goto('https://www.google.com')

        # Search for "Hans Zimmer"
        page.fill('textarea[name="q"]', 'Hans Zimmer')  # Updated selector for Google's dynamic behavior
        page.press('textarea[name="q"]', 'Enter')

        # Wait for search results to load
        page.wait_for_selector('h3')

        # Click the first link in the search results
        first_link = page.query_selector('h3')
        first_link.click()

        # Wait for the page to load and extract text
        page.wait_for_load_state('domcontentloaded')
        page_content = page.inner_text('body')
        
        h1_content = page.inner_text('h1#firstHeading.firstHeading')
        print("Extracted H1 content:", h1_content)

        # Print the extracted text from the page
        print(page_content)

        # Close the browser
        browser.close()

if __name__ == "__main__":
    run_test()
