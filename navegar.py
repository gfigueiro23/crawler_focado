from bs4 import BeautifulSoup
import requests
from lxml import html

# Navegação
class Navegar():
    def __init__(self, url, text):
        self.url = url
        self.text = str(text.replace(" ", "-")) # troca os espaços do texto digitado por "-"
        self.json = {}

        # Configuração se a url for da americadas
        if self.url == 'https://www.americanas.com.br/':
            dominio = 'https://www.americanas.com.br'  
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"}
            page = requests.get(f'https://www.americanas.com.br/busca/{self.text}', headers=headers)
            tree = html.fromstring(page.content) 
            produtos = tree.xpath('//div[@class="col__StyledCol-sc-1snw5v3-0 epVkvq src__ColGridItem-sc-122lblh-0 bvfSKS"]')

            try:
                for x in produtos:
                    nome_produto = x.xpath('.//span[@class="src__Text-sc-154pg0p-0 src__Name-sc-1k0ejj6-4 kpvRnK"]//text()')[0]
                    price = x.xpath('.//span[@class="src__Text-sc-154pg0p-0 src__PromotionalPrice-sc-1k0ejj6-8 gxxqGt"]//text()[2]')[0]
                    link = x.xpath('.//div[@class="src__Wrapper-sc-1k0ejj6-3 eflURh"]/a/@href')[0]
                    link = f'{dominio}{link}'
                    if self.json:
                        update = {nome_produto: {
                                "price": price,
                                "link": link
                            }}
                        self.json.update(update)
                    else:

                        self.json = {
                            nome_produto: {
                                "price": price,
                                "link": link
                            }
                        }
            except IndexError as e:
                print(e) 
            
    def getItem(self):
        return self.json

