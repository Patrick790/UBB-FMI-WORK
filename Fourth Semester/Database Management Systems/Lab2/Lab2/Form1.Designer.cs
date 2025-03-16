namespace Lab_1
{
    partial class Form1
    {

        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.dataGridViewParent = new System.Windows.Forms.DataGridView();
            this.dataGridViewChild = new System.Windows.Forms.DataGridView();
            this.adaugareButton = new System.Windows.Forms.Button();
            this.stergereButton = new System.Windows.Forms.Button();
            this.actualizareButton = new System.Windows.Forms.Button();
            this.messageToUser = new System.Windows.Forms.Label();
            this.panel_Child = new System.Windows.Forms.Panel();
            this.panel_Parent = new System.Windows.Forms.Panel();
            this.tableName_Parent = new System.Windows.Forms.Label();
            this.tableName_Child = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewParent)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewChild)).BeginInit();
            this.SuspendLayout();
            // 
            // dataGridViewParent
            // 
            this.dataGridViewParent.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridViewParent.Location = new System.Drawing.Point(12, 26);
            this.dataGridViewParent.Name = "dataGridViewParent";
            this.dataGridViewParent.Size = new System.Drawing.Size(261, 223);
            this.dataGridViewParent.TabIndex = 0;
            this.dataGridViewParent.RowHeaderMouseClick += new System.Windows.Forms.DataGridViewCellMouseEventHandler(this.dataGrid_Parent_RowHeaderMouseClick);
            // 
            // dataGridViewChild
            // 
            this.dataGridViewChild.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridViewChild.Location = new System.Drawing.Point(291, 26);
            this.dataGridViewChild.Name = "dataGridViewChild";
            this.dataGridViewChild.Size = new System.Drawing.Size(426, 223);
            this.dataGridViewChild.TabIndex = 1;
            this.dataGridViewChild.RowHeaderMouseClick += new System.Windows.Forms.DataGridViewCellMouseEventHandler(this.dataGrid_Child_RowHeaderMouseClick);
            // 
            // adaugareButton
            // 
            this.adaugareButton.Location = new System.Drawing.Point(338, 274);
            this.adaugareButton.Name = "adaugareButton";
            this.adaugareButton.Size = new System.Drawing.Size(75, 23);
            this.adaugareButton.TabIndex = 10;
            this.adaugareButton.Text = "Adaugare";
            this.adaugareButton.UseVisualStyleBackColor = true;
            this.adaugareButton.Click += new System.EventHandler(this.addButton_Click);
            // 
            // stergereButton
            // 
            this.stergereButton.Location = new System.Drawing.Point(338, 312);
            this.stergereButton.Name = "stergereButton";
            this.stergereButton.Size = new System.Drawing.Size(75, 23);
            this.stergereButton.TabIndex = 11;
            this.stergereButton.Text = "Stergere";
            this.stergereButton.UseVisualStyleBackColor = true;
            this.stergereButton.Click += new System.EventHandler(this.deleteButton_Click);
            // 
            // actualizareButton
            // 
            this.actualizareButton.Location = new System.Drawing.Point(338, 349);
            this.actualizareButton.Name = "actualizareButton";
            this.actualizareButton.Size = new System.Drawing.Size(75, 23);
            this.actualizareButton.TabIndex = 12;
            this.actualizareButton.Text = "Actualizare";
            this.actualizareButton.UseVisualStyleBackColor = true;
            this.actualizareButton.Click += new System.EventHandler(this.updateButton_Click);
            // 
            // messageToUser
            // 
            this.messageToUser.AutoSize = true;
            this.messageToUser.Location = new System.Drawing.Point(12, 252);
            this.messageToUser.Name = "messageToUser";
            this.messageToUser.Size = new System.Drawing.Size(35, 13);
            this.messageToUser.TabIndex = 14;
            this.messageToUser.Text = "label5";
            // 
            // panel_Child
            // 
            this.panel_Child.Location = new System.Drawing.Point(441, 268);
            this.panel_Child.Name = "panel_Child";
            this.panel_Child.Size = new System.Drawing.Size(309, 166);
            this.panel_Child.TabIndex = 17;
            // 
            // panel_Parent
            // 
            this.panel_Parent.Location = new System.Drawing.Point(12, 268);
            this.panel_Parent.Name = "panel_Parent";
            this.panel_Parent.Size = new System.Drawing.Size(302, 166);
            this.panel_Parent.TabIndex = 18;
            // 
            // tableName_Parent
            // 
            this.tableName_Parent.Location = new System.Drawing.Point(34, 9);
            this.tableName_Parent.Name = "tableName_Parent";
            this.tableName_Parent.Size = new System.Drawing.Size(100, 14);
            this.tableName_Parent.TabIndex = 19;
            this.tableName_Parent.Text = "Parent";
            // 
            // tableName_Child
            // 
            this.tableName_Child.Location = new System.Drawing.Point(313, 9);
            this.tableName_Child.Name = "tableName_Child";
            this.tableName_Child.Size = new System.Drawing.Size(100, 14);
            this.tableName_Child.TabIndex = 20;
            this.tableName_Child.Text = "Child";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.tableName_Child);
            this.Controls.Add(this.tableName_Parent);
            this.Controls.Add(this.panel_Parent);
            this.Controls.Add(this.panel_Child);
            this.Controls.Add(this.actualizareButton);
            this.Controls.Add(this.stergereButton);
            this.Controls.Add(this.adaugareButton);
            this.Controls.Add(this.dataGridViewChild);
            this.Controls.Add(this.dataGridViewParent);
            this.Controls.Add(this.messageToUser);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewParent)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewChild)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();
        }
        
        #endregion

        private System.Windows.Forms.Label tableName_Parent;
        private System.Windows.Forms.Label tableName_Child;

        private System.Windows.Forms.Panel panel_Parent;

        private System.Windows.Forms.Panel panel_Child;

        private System.Windows.Forms.DataGridView dataGridViewParent;

        private System.Windows.Forms.DataGridView dataGridViewChild;

        private System.Windows.Forms.Label messageToUser;


        private System.Windows.Forms.Button adaugareButton;
        private System.Windows.Forms.Button stergereButton;
        private System.Windows.Forms.Button actualizareButton;
    }
}

