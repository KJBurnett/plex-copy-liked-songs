import argparse
import os
import requests
from plexapi.server import PlexServer


def copyMediaPart(mediaPart, destinationPath):
    source_path = mediaPart.file
    _, filename = os.path.split(source_path)
    destination_file = os.path.join(destinationPath, filename)
    os.makedirs(
        os.path.dirname(destination_file), exist_ok=True
    )  # Ensure directory exists
    with open(destination_file, "wb") as dest_file:
        with open(source_path, "rb") as src_file:
            dest_file.write(src_file.read())


def getPlaylistSongs(plexServer, libraryName, playlistName, copy=False):
    library = plexServer.library.section(libraryName)
    playlist = library.playlist(playlistName)
    playlistSongs = []

    print(f"Collating tracks from '{playlistName}' (This can take a minute)...")

    destinationPath = playlistName  # Destination path is the same as playlist name.

    if copy:
        print(
            f"NOTE: --copy=true! Additionally copying files to destinationPath={destinationPath}. This can take some time depending on hard disk I/O read/write speeds!!!"
        )

    for track in playlist.items():
        playlistSongs.append(track.media[0].parts[0].file)

        if copy:
            for part in track.media[0].parts:
                copyMediaPart(part, destinationPath)
                print(f"Successfully copied {part.file}")

    print()  # Newline.
    if copy:
        print(
            f"Successfully collated and copied {len(playlistSongs)} songs to the destinationPath: {destinationPath}"
        )
    else:
        print(f"Successfully collated {len(playlistSongs)} to stored array.")

    return playlistSongs


def main():
    parser = argparse.ArgumentParser(
        description="Copy songs from a Plex playlist to a destination folder."
    )
    parser.add_argument("--plexApiToken", required=True, help="Plex API token")
    parser.add_argument(
        "--plexServerUrl", required=True, help="Base URL of your Plex server"
    )
    parser.add_argument(
        "--copy", action="store_true", help="Copy the files to destination path"
    )
    parser.add_argument("--musicLibrary", help="Name of the music library")
    parser.add_argument("--playlist", help="Name of the playlist to copy songs from")
    args = parser.parse_args()

    session = requests.Session()
    session.verify = False
    plexServer = PlexServer(args.plexServerUrl, args.plexApiToken, session)

    playlistSongs = getPlaylistSongs(
        plexServer, args.musicLibrary, args.playlist, args.copy
    )

    if args.copy:
        if not os.path.exists(args.playlist):
            os.makedirs(args.playlist)

        with open(f"{args.playlist}_songs.txt", "w", encoding="utf-8") as file:
            for song_path in playlistSongs:
                file.write(song_path + "\n")

        print(
            f"Successfuly wrote {len(playlistSongs)} songs from {args.playlist} playlist to {args.playlist}_songs.txt."
        )
    else:
        print(f"No songs found in {args.playlist} playlist.")

    print("\nEnd of Line.")


if __name__ == "__main__":
    main()
