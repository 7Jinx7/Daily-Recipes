# Daily Recipe Inspiration Web App
## Author: Sanjana Suresh

### Package Summary:
- This web app fetches the top recipe from the Reddit community "r/recipes" and displays it to users. 
- Users can view the recipe name and the link to the full recipe post.
- The web app uses the Reddit API to fetch the top recipe post from the r/recipes subreddit.
- It presents the recipe title and provides a link to the original recipe.
- The app uses:
   - Python 3.7+
   - Flask: To create the web application.
   - requests: For making HTTP requests to the Reddit API.
   - Jinja2: For rendering the HTML templates.


### Install and Run Instructions:
1. Install the required dependencies using `pip`:
   pip install Flask
   pip install requests

2. Check items in their appropriate directories:
   - The `index.html` file should be inside a folder called `templates`.
   - The image should be placed inside a folder called `static`.

3. Run the app using:
   python3 app.py

4. Open your browser and navigate to `http://127.0.0.1:5000/` to view the app.

### Code: 
- Flask Route (Line 22): This route is responsible for rendering the homepage, fetching the recipe data, and displaying it using index.html.
- Fetch Recipe (Line 11): This function fetches the top post from r/recipes using the Reddit API. 
- HTML Template (Line 35): The template displays the recipe's details, as well as the color scheme.

### Future Idea: 
- In a future class project, this package could be expanded to build a Recipe Finder Web App where users can input specific ingredients they have at home, and the app would suggest recipes from multiple sources based on their available ingredients.

### Credits:
- **Recipe Source**: Recipes are sourced from [r/recipes on Reddit](https://www.reddit.com/r/recipes/).
- **Image Source**: The image is an AI generated photo of pasta.

###Copyright Disclaimer:
- No copyright infringement is intended. 
- All recipes featured in this web app are sourced from r/recipes on Reddit, and full credit is given to the original authors. 
- The recipes are provided for inspiration and personal use only. 
- The app does not claim ownership of any recipes and encourages users to visit the original sources for full details.

---