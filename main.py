import os
import datetime
from mkdocs_macros.plugin import MacrosPlugin

def define_env(env):
    """
    This is the hook for defining variables, macros and filters

    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    """

    @env.macro
    def latest_articles(category=None, limit=5):
        """
        Returns a markdown list of the latest articles.
        
        :param category: The category directory to filter by (e.g., 'Tech', 'Economie', 'Science'). 
                         If None, returns articles from all these categories.
        :param limit: The maximum number of articles to return.
        """
        docs_dir = env.conf['docs_dir']
        articles = []
        
        # Categories to scan
        target_categories = ['Tech', 'Economie', 'Science']
        if category:
            if category not in target_categories:
                return f"Category '{category}' not found."
            scan_dirs = [category]
        else:
            scan_dirs = target_categories

        for cat in scan_dirs:
            cat_path = os.path.join(docs_dir, cat)
            if not os.path.exists(cat_path):
                continue
                
            for root, dirs, files in os.walk(cat_path):
                for file in files:
                    if file.endswith('.md') and file != 'index.md' and file != 'README.md':
                        file_path = os.path.join(root, file)
                        rel_path = os.path.relpath(file_path, docs_dir).replace('\\', '/')
                        
                        # Get title (first line or filename)
                        title = file[:-3].replace('-', ' ').title()
                        try:
                            with open(file_path, 'r', encoding='utf-8') as f:
                                first_line = f.readline().strip()
                                if first_line.startswith('# '):
                                    title = first_line[2:].strip()
                        except Exception:
                            pass

                        # Get date (modification time for simplicity, ideally git date)
                        # Using os.path.getmtime
                        mod_time = os.path.getmtime(file_path)
                        date_obj = datetime.datetime.fromtimestamp(mod_time)
                        
                        articles.append({
                            'title': title,
                            'path': rel_path,
                            'date': date_obj,
                            'category': cat
                        })

        # Sort by date descending
        articles.sort(key=lambda x: x['date'], reverse=True)
        
        # Determine current page directory to calculate relative links
        try:
            current_page_path = env.page.file.src_path
            current_dir = os.path.dirname(current_page_path)
        except AttributeError:
            current_dir = ""

        # Format output
        output = []
        for article in articles[:limit]:
            # Calculate link relative to the current page
            # article['path'] is relative to docs_dir (e.g. Tech/article.md)
            # We need path from current_dir to article['path']
            
            # Full path to article from docs root
            article_rel_root = article['path']
            
            # Rel path from current page
            final_link = os.path.relpath(article_rel_root, current_dir).replace('\\', '/')
            
            # Format: - [Title](path) (Category - Date)
            date_str = article['date'].strftime('%Y-%m-%d')
            if category:
                 output.append(f"- [{article['title']}]({final_link}) <small>({date_str})</small>")
            else:
                 output.append(f"- [{article['title']}]({final_link}) <small>({article['category']} - {date_str})</small>")
                 
        if not output:
            return "Aucun article trouvé."
            
        return "\n".join(output)
