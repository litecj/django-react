const initialState = {todos:[], todo:{}}
export const addTodoZction = todo => ({type:"ADD_TODO", payload:todo})

const todoReducer = (state = initialState, action) => {
    switch(action.type){
        default : return state
    }
}
export default todoReducer