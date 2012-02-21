var nodes = {};

// Compute the distinct nodes from the links.
links.forEach(function(link) {
  link.source = nodes[link.source] || (nodes[link.source] = {name: link.source});
  link.target = nodes[link.target] || (nodes[link.target] = {name: link.target});
});

var w = 1024,
    h = 700,
    r = 3;

var force = d3.layout.force()
    .nodes(d3.values(nodes))
    .links(links)
    .size([w, h])
    .linkDistance(10)
    .distance(50)
    .gravity(.05)
    .charge(-100)
    .on("tick", tick)
    .start();

var svg = d3.select("#chart").append("svg:svg")
    .attr("width", w)
    .attr("height", h);

// Per-type markers, as they don't inherit styles.
svg.append("svg:defs").selectAll("marker")
    .data(["arrow1", "arrow2", "arrow3"])
  .enter().append("svg:marker")
    .attr("id", String)
    .attr("viewBox", "0 -5 10 10")
    .attr("refX", 15)
    .attr("refY", -1.5)
    .attr("markerWidth", 4)
    .attr("markerHeight", 4)
    .attr("orient", "auto")
  .append("svg:path")
    .attr("d", "M0,-5L10,0L0,5");

var link = svg.append("svg:g").selectAll("line")
      .data(force.links());

  // Enter any new links.
  link.enter().insert("svg:line", ".node")
      .attr("class", "link")
      .attr("x1", function(d) { return d.source.x; })
      .attr("y1", function(d) { return d.source.y; })
      .attr("x2", function(d) { return d.target.x; })
      .attr("y2", function(d) { return d.target.y; })
      .attr("marker-end", function(d) { return "url(#arrow1)"; });

/*var path = svg.append("svg:g").selectAll("path")
    .data(force.links())
  .enter().append("svg:path")
    .attr("class", function(d) { return "link" })
    .attr("marker-end", function(d) { return "url(#arrow1)"; });*/

var circle = svg.append("svg:g").selectAll("circle")
    .data(force.nodes())
  .enter().append("svg:circle")
    .attr("class", "node")
    .attr("r", function(d) { return 3 + d.weight;} )
    .attr("fill", color)
    .call(force.drag)
    .on("click", function(d) { return 5 + d.weight;});

circle.append("title")
    .text(function(d) { return d.name; });

var text = svg.append("svg:g").selectAll("g")
    .data(force.nodes())
  .enter().append("svg:g");

// A copy of the text with a thick white stroke for legibility.
text.append("svg:text")
    .attr("x", -5)
    .attr("y", ".31em")
    .attr("class", "shadow")
    .text(function(d) { return (d.weight >= 10) ? d.name : ' '; });

function color(d) {
  return (d.weight >= 10) ? "#fd8d3c": "#c6dbef";
}

function tick() {

link.attr("x1", function(d) { return d.source.x; })
      .attr("y1", function(d) { return d.source.y; })
      .attr("x2", function(d) { return d.target.x; })
      .attr("y2", function(d) { return d.target.y; });

  circle.attr("cx", function(d) { return d.x = Math.max(r, Math.min(w - r, d.x)); })
        .attr("cy", function(d) { return d.y = Math.max(r, Math.min(h - r, d.y)); });

  text.attr("transform", function(d) {
    return "translate(" + d.x + "," + d.y + ")";
  });
}