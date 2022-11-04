terraform {
  required_providers {
    spotify = {
      version = "~> 0.2.6"
      source  = "conradludgate/spotify"
    }
  }
}

provider "spotify" {
  api_key = var.spotify_api_key
}

data "spotify_search_track" "by_artist" {
  artist = "Ramil"
  album  = "Сон"
  name   = "Сон"
}


data "spotify_search_track" "enrico" {
  artist = "Enrico Macias"
  album  = "Ses Plus Belles Chansons"
  name   = "Adieu mon pays"
}

data "spotify_search_track" "hemdem" {
  artist = "Sinan Cem Eroglu, Muhlis Berberoglu"
  album  = "Hemdem"
  name   = "Nesrin"
}
resource "spotify_playlist" "playlist" {
  name        = "abbabe Terraform Playlist"
  description = "This playlist was created by abbabe"
  public      = true

  tracks = [
    data.spotify_search_track.by_artist.tracks[0].id,
    data.spotify_search_track.enrico.tracks[0].id,
    data.spotify_search_track.hemdem.tracks[0].id,

  ]
}
