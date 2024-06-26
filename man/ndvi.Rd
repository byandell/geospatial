% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/ndvi.R
\name{ndviServer}
\alias{ndviServer}
\alias{ndviInput}
\alias{ndviOutput}
\alias{ndviApp}
\title{Shiny App to Stream NDVI data}
\usage{
ndviServer(id)

ndviInput(id)

ndviOutput(id)

ndviApp(title = "Stream NDVI")
}
\arguments{
\item{id}{identifier for shiny reactive}

\item{title}{title of app}
}
\value{
reactive app

reactive input

reactive input

reactive app
}
\description{
For now, this uses the default redlining GeoJSON URL to extract
cities from user-selected state(s). It is possible to put in your
own URL, but it is tricky to find these URLs.
}
