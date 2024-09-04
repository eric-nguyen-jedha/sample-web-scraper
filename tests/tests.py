from unittest.mock import patch, MagicMock
from scraper import fetch_latest_post, log_posts

# Mock the requests.get method in fetch_latest_post
@patch('requests.get')
def test_fetch_latest_post(mock_get):
    # Mock the response from requests.get
    mock_response = MagicMock()
    mock_response.content = '''
    <html>
        <body>
            <div></div> <!-- div[1] -->
            <div>
                <div>
                    <div></div>
                    <div>
                        <div class="h6">Article Title 1</div>
                        <div class="h6">Article Title 2</div>
                        <div class="h6">Article Title 3</div>
                    </div>
                </div>
            </div>
        </body>
    </html>
    '''
    mock_get.return_value = mock_response

    # Call the function
    titles = fetch_latest_post()

    # Assertions
    assert len(titles) > 0, "Expected non-empty parsed_titles"

@patch("os.makedirs")
@patch("os.path.exists")
@patch("pandas.DataFrame.to_csv")
def test_log_posts(mock_to_csv, mock_exists, mock_makedirs):
    # Prepare the test data
    posts = ['Article Title 1', 'Article Title 2', 'Article Title 3']
    
    # Mock os.path.exists to return False (so the directory does not exist)
    mock_exists.return_value = False
    
    # Call the function
    log_posts(posts)
    
    # Assertions
    mock_makedirs.assert_called_once_with("./posts")  # Check if directory creation was attempted
    mock_to_csv.assert_called_once()  # Check if the CSV file was attempted to be written
    
    # Extract the arguments passed to to_csv to further validate them
    args, kwargs = mock_to_csv.call_args
    assert kwargs['index'] == False  # Ensure index=False was passed to to_csv
    assert args[0].startswith("./posts/posts-")  # Ensure the file path starts with the correct directory and prefix