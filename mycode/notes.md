# RL  notes
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

## Markov Decision Process (MDP)
Definition: 
- the future depends only on the **present** and **not on the past**
- a probabilistic model that solely depends on the **current state** to **predict the next state**
- transition: moving from one state to another
- transition probability: the possibility of moving from one state to another

### elements
- $S$: A set of states the agent can actually be in
- $A$: A set of actions that can be performed by an agent
- $P^a_{SS'}$: transition probability of transiting from state $s$ to $s'$ by perfoming  action $a$'
- $R^a_{ss'}$: **probability** of a reward acquired by the agent for moving from state $s$ to $s'$
- $\gamma$: discount factor, controls the importance of immediate and futrue reward. 
    - $R_t=r_{t+1}+\gamma r_{t+2}+\gamma^2 r_{t+3}+\dots$
    - the future rewards are more important than immediate rewards
    - optimal value: 0.2 to 0.8

### policy function
- denoted by $\pi (s): S \rightarrow A$
- mapping from states to actions
- what action to perform in each state to **maximize the reward**
                       
### state value function
- how good it is for an agent to **be in a particular state** with a policy $\pi$
- $V^\pi(s)=E_\pi[R_t|s_t=s]$
- expected value of the reward starting from state $s$ according to policy $\pi$
- the goodness of a **state**

### State-action value function
- also known as **Q function**
- how good it is for an agent to **perform a particular action** in a state with a policy $\pi$
- $Q^\pi(s,a) = E_\pi[R_t|s_t=s, a_t=a]$
- the goodness of an **action** in a state

### Bellman equation
- solve
    - initialize random value function
    - for each state, calculate $Q(s,a)$
    - update the value function with the one which acquires maximal $Q(s,a)$
    - repeat until $V$ is optimal
