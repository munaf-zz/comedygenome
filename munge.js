var fs = require('fs'),
  _ = require('underscore'),
  comedians = require('./data/comedians.json').result,
  graph = {nodes: [], links: [], lookup: {}};

function add(comedian) {
  if (!graph.lookup[comedian]) {
    graph.nodes.push({ name: comedian });
    graph.lookup[comedian] = graph.nodes.length-1;
  }
}

// Clean up
comedians = _.filter(comedians,
  function(comedian) {
    return (comedian.influenced.length > 0) || (comedian.influenced_by.length > 0);
  });

// Transform into nodes
_.each(comedians, function(comedian) {
  add(comedian.name);
});

_.each(comedians, function(comedian, index) {
  var c = graph.lookup[comedian.name]; 

  _.each(comedian.influenced, function(influenced, index) {
    add(influenced);
    graph.links.push({ source: c, target: graph.lookup[influenced] });
  });

  _.each(comedian.influenced_by, function(influenced_by, index) {
    add(influenced_by);
    graph.links.push({ source: graph.lookup[influenced_by], target: c });
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