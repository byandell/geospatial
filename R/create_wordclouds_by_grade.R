#' Create word cloud per grade
#'
#' @param sf_object object with class `sf`
#' @param title title of wordcloud
#' @param max_size maximum size for wordcloud plot
#' @param col_select column selected from `sf_object`
#' @param min_word minimum length for word
#'
#' @return ggplot object
#' @export
#' @importFrom dplyr count filter n select ungroup
#' @importFrom tidytext unnest_tokens
#' @importFrom ggplot2 aes element_rect element_text facet_wrap ggplot ggsave
#'             labs scale_color_gradient scale_size_area theme theme_minimal
#' @importFrom grid unit
#' @importFrom ggwordcloud geom_text_wordcloud_area
#' 
create_wordclouds_by_grade <- function(sf_object,
                                       title = "Healthy food place names word cloud",
                                       max_size = 25, col_select = "name",
                                       min_word = 3) {
  # Extract relevant data and prepare text data
  text_data <- sf_object |>
    dplyr::select(grade, col_select) |>
    dplyr::filter(!is.na(col_select)) |>
    tidytext::unnest_tokens(output = "word", input = col_select, token = "words") |>
    dplyr::count(grade, word, sort = TRUE) |>
    dplyr::ungroup() |>
    dplyr::filter(dplyr::n() > 1)  # Filter to remove overly common or single-occurrence words
  
  # Ensure there are no NA values or 1-2 letter words in the 'word' column
  text_data <- text_data |> dplyr::filter(!is.na(word) & nchar(word) >= min_word)
  
  # Handle cases where text_data might be empty
  if (nrow(text_data) == 0) {
    stop("No data available for creating word clouds.")
  }
  
  # Create a word cloud using ggplot2 and ggwordcloud
  ggplot2::ggplot( ) +
    ggwordcloud::geom_text_wordcloud_area(data=text_data,
                             ggplot2::aes(label = word, size = n),
                             rm_outside = TRUE) +
    ggplot2::scale_size_area(max_size = max_size) +
    ggplot2::facet_wrap(~ grade, nrow = 1) +
    ggplot2::scale_color_gradient(low = "darkred", high = "red") +
    ggplot2::theme_minimal() +
    ggplot2::theme(
      plot.background = ggplot2::element_rect(fill = "white", color = NA),
        panel.background = ggplot2::element_rect(fill = "white", color = NA),
        panel.spacing = grid::unit(0.5, "lines"),
        plot.title = ggplot2::element_text(size = 16, face = "bold"),
        legend.position = "none") +
    ggplot2::labs(title = title)
}
