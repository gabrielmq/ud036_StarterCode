import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content=", chorme=1">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" 
        href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" 
        href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script 
        src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script 
        src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        * {
            margin: 0;
            padding: 0;
            outline: 0;
            box-sizing: border-box;
        }
        body {
            font-family: "Roboto", "Ubuntu", "Molengo", sans-serif;
            padding-top: 80px;
            background-color: #f8f9fa;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            background-color: #f8f9fa;
            width: 375px;
            margin-right: 5px;
            margin-bottom: 20px;
            padding: 15px 15px;
            border-radius: 5px;
            border: 0 none;
            box-shadow: 0px 2px 5px 0px rgba(0,0,0,0.5);
            transform: scale(0.9);
        }
        img {
            display: block;
            width: 100%;
            height: auto;
        }
        .poster_image {
            position: absolute;
            top: 0;
            bottom: 0;
            left: 0;
            right: 0;
            height: 100%;
            width: 100%;
            opacity: 0;
            transition: .5s ease;
            background-color: #242627;
        }
        .text-info {
            color: #fff;
            margin: 0 auto;
            margin-top: 200px;
        }
        .card:hover .poster_image {
            opacity: 0.9;
        }
        .aumentar-card {
            transition: all .2s ease-in-out;
            transform: scale(1);
        }
        .diminuir-card {
          transition: all .2s ease-in-out;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .show-trailer-bg-color {
            color: #fed136;
        }
        .show-trailer-bg-color:hover {
            color: #ccc;
        }
        .site-name {
            padding: 5px;
            font-size: 26px;
            margin-bottom: 10px;
            color: #fed136;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.card a', function (event) {
            const trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            const sourceUrl = 'https://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("slow", function showNext() {
            $(this).next("div").show("slow", showNext);
          });
        });

        // aplica o efeito que aumenta o card
        $(document).on('mousemove', 'div .movie-tile', function() {
          $(this).addClass("aumentar-card");
          $(this).removeClass("diminuir-card");
        });

        // aplica o efeito que diminui o card
        $(document).on('mouseout', 'div .movie-tile', function () {
          $(this).addClass("diminuir-card");
          $(this).removeClass("aumentar-card");
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" 
           style="padding: 15px;" 
           role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand site-name" 
               style="color: #fed136;" 
               href="#">
               Fresh Tomatoes Movie Trailers
            </a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
    <div class="col-md-6 col-lg-4 movie-tile text-center">
        <div class="card" style="height: 545px;">
            <img class="card-img img-fluid" 
                src="{poster_image_url}" 
                width="220" height="342" 
                alt="{movie_title}">
            <div class="card-body poster_image">
                <div class="text-info">
                    <h2 class="card-title">{movie_title}</h2>
                    <h4 class="card-text">Director: {director}</h4>
                    <h4 class="card-text">Release Date: {release_date}</h4>
                    <h4 class="card-text">Runinng Time: {runtime}</h4>
                    <a href="#trailer" 
                        class="btn btn-link btn-lg show-trailer-bg-color"
                        data-trailer-youtube-id="{trailer_youtube_id}" 
                        data-toggle="modal" data-target="#trailer">
                        Show Trailer
                    </a>
                </div>
            </div>
        </div>
    </div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            director=movie.director,
            release_date=movie.release_date,
            runtime=movie.runtime
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open(url, new=2)
