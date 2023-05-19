RL  notes
## terminologies
- agent
    - the software programs that **make intelligent decisions**
    - learners in RL
    - interact with the environment and get rewards base on their actions.
- policy function
    - the agent's behavior in an environment
    - the way in which the agent decides **which action to perform**
- value function
     - denotes **how good it is** for an agent to be in **a particular state**'
- spaces
     - `Box`:  n-dimensional **continuous** space with **upper and lower limits** which describe the valid values our observations can take
     - `Discrete`: possible values of obsercation or action:\{0,1, ...,n-1}
        - there is only a **finite state of actions availiable**
     - `Dict`: a dictionary of simple spaces
     - `Tuple`: a uple of simple spaces
     - `MultiBinary`: an n-shape binary space
     - `MultiDiscrete`: a **series** of `Discrete` action spaces with a **different number of actions** in each element

## gymnasium functions
- `make`
    -  `render_mode`: how the environment should be visualized
- `reset`
    - returns the first observation of the environment
    - initializes the environment with a particular random seed or options
- `step`
    - performs an action in the environment
    - reveives a **new observation** from the updated environment along with a **reward** for taking the action
    
    - return values
        - `observation`: the object representing an observation of the **environment**
        - `reward`: the reward gained bt the **previous** action
        - `done`: a boolean values that indicates whether the episode has completed  
        - `info`L the information that is useful for debugging

## TensorFlow
- variables
    - containers used to store **values**
    - used as **input** to other operations in the computational graph
- constants
    - cannot have their values changed
- placeholders
    - variables where you only define the **type and demensions**, but not assign the value
- computational graph
    - consists of nodes and edges
        - nodes: the **mathematical operations**
        - edges: the tensors
- sessions
    - to execute the computational graph
    - created by calling `tf.Session()`
    - there is no `Session()` function in tensorflow v2, solve this problem by adding
    ```\
        tf.compat.v1.disable_eager_execution()
        sess = tf.compat.v1.Session()
    ```
    - run by calling `tf.run()`
- FileWriter
    - draw the computational graph
    ```
    writer = tf.compat.v1.summary.FileWriter("output", sess.graph) # v2 does not have `summary.FileWriter()` function
    print(sess.run(node))
    writer.close()
    ```
    - show the graph by typing `tensorboard --logdir=output --port=6020` in terminal
