import sklearn
from sklearn import tree
import re
import json

def DecisionTreeSerializer(decision_tree, feature_names=None, minify=True, sunburst=False):
 
  js = ""
  if(sunburst==True):
    formatstr_inner_node = '"predicate": { "field" : "%s", "operator" : "%s", "value": %s}, "error": %s, "samples": %s, "type":"split"'
    formatstr_leaf_node = '"samples": %s, "value": %s, "error": %s ,"type":"leaf"'
  else:
    formatstr_inner_node = '"label": "%s %s %s", "error": %s, "samples": %s, "type":"split"'
    formatstr_leaf_node = '"samples": %s, "value": [%s], "error": %s ,"type":"leaf"'
 
  def node_to_str(tree, node_id, criterion):
    if not isinstance(criterion, sklearn.tree.tree.six.string_types):
      criterion = "impurity"
 
    value = tree.value[node_id]
    if tree.n_outputs == 1:
      value = value[0, :]
 
    jsonValue = ', '.join([str(x) for x in value])
 
    if tree.children_left[node_id] == sklearn.tree._tree.TREE_LEAF:
      return formatstr_leaf_node \
             % (tree.n_node_samples[node_id],
                jsonValue,
                tree.impurity[node_id])
    else:
      if feature_names is not None:
        feature = feature_names[tree.feature[node_id]]
      else:
        feature = tree.feature[node_id]
 
      if "=" in feature:
        ruleType = "="
        ruleValue = "false"
      else:
        ruleType = "<="
        ruleValue = "%.4f" % tree.threshold[node_id]
 
      return formatstr_inner_node \
             % (feature,
                ruleType,
                ruleValue,
                #criterion,
                tree.impurity[node_id],
                tree.n_node_samples[node_id])
 
  def recurse(tree, node_id, criterion, parent=None, depth=0):
    tabs = "  " * depth
    js = ""
 
    left_child = tree.children_left[node_id]
    right_child = tree.children_right[node_id]
 
    js = js + "\n" + \
         tabs + "{\n" + \
         tabs + "  " + node_to_str(tree, node_id, criterion)
 
    if left_child != sklearn.tree._tree.TREE_LEAF:
      js = js + ', "children": {'
      js = js + "\n" + \
           tabs + '  "0": ' + \
           recurse(tree, \
                   left_child, \
                   criterion=criterion, \
                   parent=node_id, \
                   depth=depth + 1) + ",\n" + \
           tabs + '  "1": ' + \
           recurse(tree, \
                   right_child, \
                   criterion=criterion, \
                   parent=node_id,
                   depth=depth + 1) + "}"
 
    js = js + tabs + "\n" + \
         tabs + "}"
 
    return js
 
  if isinstance(decision_tree, sklearn.tree.tree.Tree):
    js = js + recurse(decision_tree, 0, criterion="impurity")
  else:
    js = js + recurse(decision_tree.tree_, 0, criterion=decision_tree.criterion)
  return json.loads(js)

  
  




  
  
