package com.fv.novella.utilits

import androidx.fragment.app.Fragment
import com.fv.novella.MainActivity
import com.fv.novella.R

lateinit var APP_ACTIVITY: MainActivity

fun replaceFragment(fragment: Fragment, addStack:Boolean = true){
    if (addStack){
        APP_ACTIVITY.supportFragmentManager.beginTransaction()
            .addToBackStack(null)
            .replace(
                R.id.dataContainer,
                fragment
            ).commit()
    } else {
        APP_ACTIVITY.supportFragmentManager.beginTransaction()
            .replace(R.id.dataContainer,
                fragment
            ).commit()
    }
}