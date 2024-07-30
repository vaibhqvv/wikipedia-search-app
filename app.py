from flask import Flask, request, render_template
import wikipediaapi

app = Flask(__name__)

# home route
@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        search = request.form["search"]
        user_agent = "Wikipedia-Search-App (voidsyntaxes@gmail.com)"
        wiki_wiki = wikipediaapi.Wikipedia(
            language='en', 
            user_agent=user_agent
        )
        try:
            # Fetch data from wikipedia
            page = wiki_wiki.page(search)
            if(page.exists):
                result = page.summary[:10000] #get first 1000 characters of summary
            else:
                result = "The page doesn't exist on Wikipedia."
        except Exception as e:
            result = f"An error occured: {str(e)}"
        
        return render_template("result.html", result=result)
            
    
if __name__ == '__main__':
    app.run(debug=True)