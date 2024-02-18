import justpy as jp


class About:
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the About page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""
        Welcome to Instant-Dictionary, where language meets convenience.
                Our web application is designed to make accessing definitions and expanding your vocabulary easier than ever 
                before. Whether you're a student looking to enhance your understanding of academic texts, a professional 
                seeking precision in your writing, or simply someone curious about the nuances of language, our instant 
                dictionary is here to serve you.
                """, classes='text-lg')

        return wp

