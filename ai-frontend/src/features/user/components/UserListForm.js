import React from "react"

const UserListForm = ({list}) => {

    return (<>
        <table  border='1px' style={{textAlign:'center'}}>
            <thead>
                    <tr>
                        <th>사용자 아이디</th>
                        <th>사용자 이름</th>
                        <th>사용자 생년월일</th>
                        <th>사용자 주소</th>
                        <th>사용자 이메일</th>
                    </tr> 
            </thead> 
            <tbody>
                {list.map((users)=>(
                    <tr>
                        <td>{users.username}</td>
                        <td>{users.name}</td>
                        <td>{users.birth}</td>
                        <td>{users.address}</td>
                        <td>{users.email}</td>
                    </tr>                
                ))}
            </tbody>
        </table>
    </>)
}
// 누군가의 자식이기에 function 이 아니라 람다식으로 사용
export default UserListForm