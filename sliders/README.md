Slider Recipes
==============

I need to control the year start and year end for an interaction, and
year start should always be less than year end.  How to do?

* `a_basic.py` - gets the sliders in place

* `b_update_end.py` - gets the start year right when end year changes

* `c_update_start_and_end.py` - natural extension to get start and end
  right when the other changes, but that doesn't work

* `d_update_end_on_start_and_end.py` - another try, but also doesn't
  work

I think what I am trying to do is not yet possible:
https://community.plot.ly/t/both-input-and-output/5674/6 (2019-01-03)

Oh! Actually, there is a widget for what I want already:
https://dash.plot.ly/dash-core-components/rangeslider

* `e_batteries_included.py` - turns out that there was a better widget
  for my goals

To run: `python [filename.py]`, then point web browser to url this
prints.