# plex-copy-liked-songs
A helper tool that can list or copy your liked songs based on star ratings to another directory. Useful for moving your favorite music to a CD or a thumb drive.

# How to Run This Script

This guide will walk you through the steps to install Python and run the Plex Playlist Copy Script on your server. Please note that the script must be run on the server where your Plex server is hosted in order to work properly.

## Prerequisites

Before running the script, make sure you have completed the following steps:

1. **Install Python**: If you don't already have Python installed on your server, follow the steps outlined in the [Python Installation](#step-1-install-python) section below.

2. **Create Smart Playlist**: Create a smart playlist in your Plex server containing all songs rated 4 stars or higher. This playlist will be used as the source for copying songs. Here's how to create the smart playlist:

    - Open your Plex server in a web browser.
    - Go to the "Music" section and select "Playlists".
    - Click on the "+" icon to create a new playlist.
    - Name the playlist (avoid special characters like &, or emojis) and set the following filter:
        - Filter by "Rating" is "greater than or equal to" 4 stars.
    - Save the playlist.

3. **Get Plex API Token**: Obtain a Plex API token, which is required to access the Plex server's API. Follow these steps to get your Plex API token:

    - Open a web browser and go to [https://plex.tv](https://plex.tv).
    - Log in to your Plex account.
    - Click on your profile icon in the top right corner and select "Account" from the dropdown menu.
    - In the left sidebar, click on "Access" under "Settings".
    - Scroll down to the "Plex API" section and click on "Show".
    - Copy the displayed API token.

## Step 1: Install Python

If you don't already have Python installed on your server, follow these steps to install it:

1. **Linux**: Most Linux distributions come with Python pre-installed. You can check if Python is installed by running the following command in your terminal:

    ```bash
    python --version
    ```

    If Python is installed, you'll see its version number. If not, you can install Python using your package manager. For example, on Ubuntu, you can install Python 3 with the following command:

    ```bash
    sudo apt-get update
    sudo apt-get install python3
    ```

2. **Windows**: Visit the [Python Downloads](https://www.python.org/downloads/) page, download the latest version of Python for Windows, and run the installer. Make sure to check the box that says "Add Python to PATH" during installation.

## Step 2: Download the Script

Download the Plex Playlist Copy Script from the [GitHub repository](https://github.com/your/repository). You can either clone the repository or download the script directly as a ZIP file.

## Step 3: Install Dependencies

The script requires the `requests` and `plexapi` libraries. You can install them using `pip`, the Python package manager. Open your terminal and run the following commands:

```bash
pip install requests plexapi
```

## Step 4: Run the Script

Once you've installed Python and the required dependencies, you can run the script. Here's how to do it:

1. Open your terminal or command prompt.

2. Navigate to the directory where you downloaded the script using the `cd` command. For example:

    ```bash
    cd path/to/script/directory
    ```

3. Run the script using the following command:

    ```bash
    python plex_playlist_copy.py --plexApiToken YOUR_PLEX_API_TOKEN --plexServerUrl YOUR_PLEX_SERVER_URL --copy --musicLibrary YOUR_MUSIC_LIBRARY_NAME --playlist YOUR_PLAYLIST_NAME
    ```

    Replace `YOUR_PLEX_API_TOKEN` with your Plex API token, `YOUR_PLEX_SERVER_URL` with the base URL of your Plex server, `YOUR_MUSIC_LIBRARY_NAME` with the name of your music library in Plex, and `YOUR_PLAYLIST_NAME` with the name of the playlist you want to copy songs from.

    For example:

    ```bash
    python plex_playlist_copy.py --plexApiToken abc123 --plexServerUrl http://localhost:32400 --copy --musicLibrary Music --playlist MyPlaylist
    ```

4. Press Enter to execute the command. The script will start running and copy the songs from the specified playlist to a destination folder.

5. Once the script has finished running, you'll see a message indicating that the process is complete.

## Important Note

Ensure that you run the script on the server side where your Plex server is hosted. Attempting to run the script on a different machine may result in file path issues.

That's it! You've successfully copied songs from your Plex playlist to a destination folder using the script. The folder should be in the same path as the script that was ran.
