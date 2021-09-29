const initialState = {users:[], user:{}}
export const addUserAction = user => ({type: 'ADD_USER', payload: user})
const userReducer = (state = initialState, action)  => {
    switch(action.type){
        case 'ADD_USER': return {...state, users:[...state.users, action.payload]}
        default : return state
    }
}
export default userReducer