import scrapy

class KeneshScrapy(scrapy.Spider):
    name = 'kenesh'
    start_urls = ['http://kenesh.kg/ru/deputy/list/35']
    
    def parse(self, response):
        deputats = response.css('div.dep-item')
        
        for deputat in deputats:
            full_name = deputat.css('a.name::text').get()
            image = deputat.css('img::attr(src)').get()
            fraction = deputat.css('div.info::text').get()    
            phone_call = deputat.css('a.phone-call::attr(href)').get()
            mail = deputat.css('a.mail::attr(href)').get()
            
            if phone_call:
                phone_call = phone_call.replace('tel:', '').strip()
            
            if mail:
                mail = mail.replace('mailto:', '').strip()
                
            yield{
                "full_name": full_name,
                "image": "http://kenesh.kg/" + image,
                "fraction": fraction,
                "phone_call": phone_call,
                "mail": mail
                }
        next_page = response.css("a.next::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)