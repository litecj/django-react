const initialState = {userus:[], useru:{}}
export const addUserAction2 = useru => ({type:"ADD_USER", payload: useru})
export const changePasswordAction = useru => ({type:"EDIT_PW", payload: useru})

const userUpReducer = (state = initialState, action) => {
    switch(action.type) {
        case "ADD_USER" :
            return {...state, userus:[...state.userus, action.payload]}
        case "EDIT_PW" :
            // alert("email : " + action.payload.email +" // pw : " + action.payload.pw)
            return {...state, userus: state.userus.map(
                useru => (useru.email === action.payload.email ?
                    {...useru, password : action.payload.password} : useru))}
        default : return state
    }
}
export default userUpReducer