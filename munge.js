var fs = require('fs'),
  comedians = require('./data/comedians.json').result,
  graph = {nodes: [], links: [], lookup: {}};

function add(comedian) {
  if (!graph.lookup[comedian]) {
    graph.nodes.push({ name: comedian });
    graph.lookup[comedian] = graph.nodes.length-1;
  }
}

// Remove stray nodes
comedians = comedians.filter(function(comedian) {
  return (comedian.influenced.length > 0) || (comedian.influenced_by.length > 0);
});

// Add nodes to graph
comedians.forEach(function(comedian) {
  add(comedian.name);
});

// Add edges to graph
comedians.forEach(function(comedian) {
  var node = graph.lookup[comedian.name];

  comedian.influenced.forEach(function(influenced) {
    add(influenced);
    graph.links.push({ source: node, target: graph.lookup[influenced] });
  });

  comedian.influenced_by.forEach(function(influencer) {
    add(influencer);
    graph.links.push({ source: graph.lookup[influencer], target: node });
  });

});

// Remove temp name lookup object
delete graph.lookup;

// Output file
fs.writeFile('data/comedian-graph.json', JSON.stringify(graph, null, 2), function(err) {
  if (err) {
    console.log(err);
  }
});
