# econ-sim
An attempt to simulate markets and economies in python.

The end goal is to be able to simulate economies, either for research or for use in games as the engine for a real & dynamic economy.

To start with though we are focusing on simulating a single market.

The difference in simulating a market, compared to the kind of analysis one does on markets in introductory economics classes, is that the market simulation has a time parameter. Tradtionally we just look at markets at a specific point in time with a specific price and quantity value. When we talk about this price/quantity equilibrrium changing (for example due to price controls) we do not think about the time it takes for these changes to occur; we just look at the start and end values. 

Obviously, simulating a market is a bit more complicated. Normally, we would just need to know the Supply and Demand curve functions to find p and q. Now though p and q are dynamic variables with a parameter variable t for time. Furthermore, not only do we need to know the initial supply and demand functions but we need to know how these functions change with respect to time. Finally, we need to know the response time of the market participants. This is some value that represents the amount of time units it takes for a given market to move to it's equilibrium from a point of being out of equilirbrium. This takes into account things like the delay from when a positive demand shock happens to when suppliers realize it and account for it with higher prices.  


Add Parameters to simulation:
-Raw Materials in economy.

-Advanced Products and their raw material recipes.

-Economics agents Eg: merchants, governments, corporations.
