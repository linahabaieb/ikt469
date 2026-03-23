import scrapy
from assignment_9.items import CourseItem

# Spider for scraping course information from the UIA website.
class CourseSpider(scrapy.Spider):
    name = "courses"
    allowed_domains = ["uia.no"]
    
    # 14 links to course pages for the years 2024, 2025, and 2026.
    start_urls = [
        "https://www.uia.no/studier/emner/2026/var/ikt103.html",
        "https://www.uia.no/studier/emner/2026/var/ikt104.html",
        "https://www.uia.no/studier/emner/2026/var/ikt105.html",
        "https://www.uia.no/studier/emner/2026/var/ikt204.html",
        "https://www.uia.no/studier/emner/2024/host/ikt201.html",
        "https://www.uia.no/studier/emner/2025/host/ikt202.html",
        "https://www.uia.no/studier/emner/2025/host/ikt203.html",
        "https://www.uia.no/studier/emner/2026/var/ikt205.html",
        "https://www.uia.no/studier/emner/2026/var/ikt206.html",
        "https://www.uia.no/studier/emner/2026/var/ikt218.html",
        "https://www.uia.no/studier/emner/2025/host/ikt211.html",
        "https://www.uia.no/studier/emner/2025/host/ikt213.html",
        "https://www.uia.no/studier/emner/2025/host/ikt222.html",
        "https://www.uia.no/studier/emner/2025/host/ikt300.html",
    ]
    
    # Method for cleaning and joining text from lists.
    @staticmethod
    def clean_text_list(texts):
        return " ".join(t.strip() for t in texts if t.strip())

    # Method for parsing and extracting relevant information from each course page.
    def parse(self, response):
        title = response.css("h1::text").get(default="").strip()
        emnekode = response.url.split("/")[-1].replace(".html", "").upper()
        
        headings = [
            h.strip()
            for h in response.css("h1::text, h2::text, h3::text").getall()
            if h.strip()
        ]
        
        body_text = self.clean_text_list(response.css("body *::text").getall())
        
        yield CourseItem(
            emnekode=emnekode,
            tittel=title,
            overskrifter=headings,
            innhold=body_text,
            url=response.url,
        )
        
        self.logger.info(f"Scraped: {emnekode}")